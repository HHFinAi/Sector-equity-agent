"""All-sector routing, evidence segregation and valuation regression tests. No live services."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from sector_agent.contracts import ROOT, load_json, validate_brief, ValidationError
from sector_agent.engine import build_plan, export_plan, run, verify, approve
from sector_agent.routing import resolve, stage_prompt, context_for, coverage, validate_scope
from sector_agent.sector_data import CATALOG
from sector_agent.valuation import value_models
from sector_agent.provider import DemoProvider
from test_agent import valid_stage


def all_brief(): return load_json(ROOT/'examples/demo-all-sectors.json')


def one(sid):
    b=all_brief();b['sector']=sid
    b['universe']=[e for e in b['universe'] if e['sector']==sid]
    b['sources']=[s for s in b['sources'] if sid in s['sector_ids']]
    b['valuation_models']=[m for m in b['valuation_models'] if m['entity']==b['universe'][0]['id']]
    b['workflow']='sector-deep-dive'
    return b


class AllSectorTests(unittest.TestCase):
    def test_eleven_major_sectors_and_79_custom_subsectors(self):
        self.assertEqual(len(CATALOG['sectors']),11)
        self.assertEqual(sum(len(s['subsectors']) for s in CATALOG['sectors'].values()),79)
        self.assertEqual(len({s['sector_code'] for s in CATALOG['sectors'].values()}),11)

    def test_every_subsector_has_a_distinct_research_lens_and_kpis(self):
        lenses=set()
        for s in CATALOG['sectors'].values():
            for sub in s['subsectors'].values():
                self.assertNotIn(sub['research_lens'],lenses);lenses.add(sub['research_lens'])
                self.assertGreaterEqual(len(sub['kpis']),4)
                self.assertTrue(sub['valuation_methods'])

    def test_each_sector_contains_transmission_materiality_sources_and_questions(self):
        for sid,p in CATALOG['sectors'].items():
            with self.subTest(sector=sid):
                for key in ('transmission_tests','materiality_tests','primary_source_requests','analytical_traps','diligence_questions'):
                    self.assertGreaterEqual(len(p[key]),2)

    def test_cross_sector_plan_expands_eleven_actual_specialist_stages(self):
        plan=build_plan(all_brief())
        self.assertEqual(len(plan['stages']),25)
        self.assertEqual(len([s for s in plan['stages'] if s.startswith('specialist_')]),11)
        self.assertEqual(plan['stages'][-2:],['challenge','synthesis'])

    def test_single_sector_and_multiple_sector_selection(self):
        b=one('financials');self.assertEqual(resolve(b)['sector_ids'],['financials'])
        b=all_brief();b.update(sector='multi',sectors=['financials','real-estate'])
        self.assertEqual(resolve(b)['sector_ids'],['financials','real-estate'])

    def test_unknown_duplicate_or_missing_multiple_selection_rejected(self):
        for values in (None,[],['financials'],['financials','financials'],['financials','fake']):
            b=all_brief();b.update(sector='multi',sectors=values)
            with self.subTest(values=values),self.assertRaises(ValidationError): resolve(b)

    def test_no_silent_healthcare_default(self):
        b=all_brief();b.pop('sector')
        with self.assertRaises(ValidationError): resolve(b)

    def test_entity_must_name_sector_in_all_mode(self):
        b=all_brief();b['universe'][0].pop('sector')
        with self.assertRaisesRegex(ValidationError,'explicit selected sector'): validate_brief(b,demo=True)

    def test_subsector_cannot_be_assigned_to_wrong_sector(self):
        b=all_brief();b['universe'][0]['subsector']='banks'
        with self.assertRaisesRegex(ValidationError,'subsector'): validate_brief(b,demo=True)

    def test_unknown_source_entity_or_sector_rejected(self):
        for key in ('entity_ids','sector_ids'):
            b=all_brief();b['sources'][0][key]=['NOT-A-REAL-ID']
            with self.subTest(key=key),self.assertRaisesRegex(ValidationError,'scope ID'): validate_brief(b,demo=True)

    def test_unscoped_evidence_does_not_fill_all_sector_gaps(self):
        b=all_brief()
        for s in b['sources']: s.pop('sector_ids');s.pop('entity_ids')
        c=coverage(b,resolve(b));self.assertTrue(all(x['gaps'] for x in c.values()))

    def test_global_macro_record_does_not_count_as_company_primary_coverage(self):
        b=all_brief();b['sources']=b['sources'][:1]
        s=b['sources'][0];s.pop('sector_ids');s.pop('entity_ids');s['global_context']=True
        c=coverage(b,resolve(b));self.assertTrue(all(x['gaps'] for x in c.values()))

    def test_specialists_receive_only_own_companies_sources_and_global_context(self):
        b=all_brief();p=resolve(b)
        for sid in p['sector_ids']:
            c=context_for('specialist_'+sid,b,p,value_models(b),{'mandate':{},'specialist_energy':{}})
            self.assertEqual({e['sector'] for e in c['brief']['universe']},{sid})
            self.assertEqual(len(c['brief']['sources']),1)
            self.assertEqual(set(c['previous_stages']),{'mandate'})
            self.assertEqual(len(c['computed_valuations']),1)

    def test_all_sector_pack_mutation_does_not_change_catalog(self):
        p=resolve(all_brief());p['sectors']['financials']['name']='tampered'
        self.assertEqual(CATALOG['sectors']['financials']['name'],'Financials')

    def test_prompts_really_contain_sector_specific_lenses(self):
        p=resolve(all_brief())
        self.assertIn('deposit beta',stage_prompt('specialist_financials',p))
        self.assertIn('cap rate',stage_prompt('specialist_real-estate',p))
        self.assertIn('spectrum',stage_prompt('specialist_communication-services',p))
        self.assertIn('ore',stage_prompt('specialist_materials',p).lower())

    def test_all_twelve_workflows_export_with_all_sectors(self):
        flows=load_json(ROOT/'workflows/catalog.json');self.assertEqual(len(flows),12)
        with tempfile.TemporaryDirectory() as t:
            for flow in flows:
                b=all_brief();b['workflow']=flow
                p=export_plan(b,Path(t)/flow)
                self.assertEqual(len(list((Path(t)/flow).glob('*-specialist_*.md'))),11)
                self.assertEqual(p['stages'][-2:],['challenge','synthesis'])

    def test_end_to_end_all_sector_demo_and_ledgers(self):
        with tempfile.TemporaryDirectory() as t:
            out=Path(t)/'demo';r=run(all_brief(),DemoProvider(),out)
            self.assertEqual(r['status'],'DEMO');self.assertEqual(len(r['stages']),25)
            self.assertEqual(len(r['valuations']),11);self.assertEqual(len(r['coverage']),11)
            self.assertTrue((out/'sector-matrix.csv').exists());self.assertTrue((out/'claim-ledger.csv').exists())
            self.assertTrue(verify(out)['verified'])
            self.assertIn('Not applicable',(out/'report.md').read_text())
            with self.assertRaises(ValidationError): approve(out,'test','fixture only',True)

    def test_missing_sector_source_forces_blocked_even_when_llm_says_continue(self):
        b=all_brief();b['sources']=b['sources'][:-1];b['valuation_models']=[]
        for s in b['sources']: s['kind']='company';s['url']='https://example.org/mock-not-evidence'
        class Scripted:
            name='test';model='mock-not-live';calls=0;usage=[]
            def generate(self,stage,instructions,context):
                v=valid_stage();ids=[s['id'] for s in context['brief']['sources']]
                v['claims'][0].update(kind='assumption',source_ids=ids[:1]);return v
        with tempfile.TemporaryDirectory() as t:
            r=run(b,Scripted(),Path(t)/'run')
            self.assertEqual(r['status'],'BLOCKED')
            self.assertTrue(r['coverage']['real-estate']['gaps'])

    def test_cross_sector_citation_leakage_is_rejected(self):
        class Leaky:
            name='demo';model='mock';calls=0;usage=[]
            def generate(self,stage,instructions,context):
                v=valid_stage();v['claims'][0]['source_ids']=['S01'];return v
        with tempfile.TemporaryDirectory() as t,self.assertRaisesRegex(ValidationError,'unknown source'):
            run(all_brief(),Leaky(),Path(t)/'run')

    def test_matrix_tampering_invalidates_manifest(self):
        with tempfile.TemporaryDirectory() as t:
            out=Path(t)/'run';run(all_brief(),DemoProvider(),out)
            (out/'sector-matrix.csv').write_text('edited')
            with self.assertRaises(ValidationError): verify(out)

    def test_exported_specialist_mandate_is_scoped_like_runtime(self):
        with tempfile.TemporaryDirectory() as t:
            out=Path(t)/'plan';export_plan(all_brief(),out)
            content=next(out.glob('*-specialist_financials.md')).read_text()
            self.assertIn('Fictional Financials Company',content)
            self.assertNotIn('Fictional Energy Company',content)


class SectorValuationTests(unittest.TestCase):
    def test_all_eleven_demo_models_run(self): self.assertEqual(len(value_models(all_brief())),11)

    def test_model_cannot_borrow_unrelated_sector_source(self):
        b=all_brief();b['valuation_models'][0]['source_ids']=['S02']
        with self.assertRaisesRegex(ValidationError,'scoped to its sector'): value_models(b)

    def test_bank_cannot_use_ev_ebitda(self):
        b=one('financials');b['valuation_models'][0]['method']='multiple'
        with self.assertRaisesRegex(ValidationError,'not appropriate'): value_models(b)

    def test_regulated_utility_cannot_use_generic_ev_ebitda(self):
        b=one('utilities');b['valuation_models'][0]['method']='multiple'
        with self.assertRaisesRegex(ValidationError,'not appropriate'): value_models(b)

    def test_bank_price_to_tangible_book_values_equity_directly(self):
        b=one('financials');m=b['valuation_models'][0];m['debt']=999999;m['cash']=777777
        v=value_models(b)[0]
        self.assertAlmostEqual(v['expected_value_per_share'],.25*15+.5*21.6+.25*28)
        self.assertTrue(all(s['enterprise_value'] is None for s in v['scenarios']))

    def test_pe_values_equity_without_an_extra_net_debt_bridge(self):
        v=value_models(one('utilities'))[0];self.assertAlmostEqual(v['expected_value_per_share'],24.5)

    def test_nav_values_cash_noi_and_deducts_all_claims(self):
        v=value_models(one('real-estate'))[0]
        self.assertAlmostEqual(v['scenarios'][0]['value_per_share'],(80/.08+50-200-20)/100)

    def test_invalid_nav_cap_rate_rejected(self):
        for cap in (0,-.02,1):
            b=one('real-estate');b['valuation_models'][0]['scenarios'][0]['properties'][0]['cap_rate']=cap
            with self.subTest(cap=cap),self.assertRaises(ValidationError): value_models(b)

    def test_duplicate_nav_property_rejected(self):
        b=one('real-estate');p=b['valuation_models'][0]['scenarios'][0]['properties'];p.append(p[0].copy())
        with self.assertRaisesRegex(ValidationError,'Duplicate NAV'): value_models(b)

    def test_ffo_and_affo_use_reconciled_per_share_inputs(self):
        for method,key in [('ffo','ffo_per_share'),('affo','affo_per_share')]:
            b=one('real-estate');m=b['valuation_models'][0];m['method']=method
            m['scenarios']=[{'name':n,'probability':w,key:x,'multiple':10} for n,w,x in [('bear',.25,1),('base',.5,2),('bull',.25,3)]]
            self.assertAlmostEqual(value_models(b)[0]['expected_value_per_share'],20)

    def test_ddm_has_equity_discount_rate_and_no_debt_bridge(self):
        b=one('utilities');m=b['valuation_models'][0];m['method']='ddm'
        m['scenarios']=[{'name':n,'probability':w,'dividends_per_share':[x],'cost_of_equity':.1,'terminal_growth':0} for n,w,x in [('bear',.25,1),('base',.5,2),('bull',.25,3)]]
        self.assertAlmostEqual(value_models(b)[0]['expected_value_per_share'],20)

    def test_negative_earnings_are_not_forced_into_pe(self):
        b=one('utilities');b['valuation_models'][0]['scenarios'][0]['eps']=-1
        with self.assertRaisesRegex(ValidationError,'positive'): value_models(b)

    def test_invalid_weights_and_unknown_model_sources_rejected(self):
        for change in ('weight','source'):
            b=one('utilities');m=b['valuation_models'][0]
            if change=='weight':m['scenarios'][0]['probability']=.9
            else:m['source_ids']=['invented']
            with self.subTest(change=change),self.assertRaises(ValidationError): value_models(b)


if __name__=='__main__': unittest.main()
