# Healthcare Equity Analyst Prompt Library

A 113-prompt research library covering healthcare sub-sectors and institutional
workflows. Existing analytical content and standing source-governance instructions
are preserved. This release adds independently addressable prompt files, a
lossless compiled-library build and an explicit evaluation protocol.

## Start here

Apply [standing instructions](library/standing_instructions.md), followed by the
[current reliability contract](library/reliability_contract.md), then the chosen
prompt from `prompts/<ID>.md`. The reliability contract qualifies legacy confidence
and platform assumptions without silently rewriting the analytical catalogue.
Supply authorized primary evidence and identify missing inputs before analysis.

`library/manifest.json` is the machine-readable ordered index of prompt IDs,
titles and paths. `library/healthcare_prompt_library.md` is generated from individual
prompt files plus `library/sections/` context. Edit the parts, not the compiled file.

```bash
python tools/library_build.py check
python tools/library_build.py build
python -m unittest discover -s tests -v
```

For initial migration only, `python tools/library_build.py init` creates the
113 prompt files and context sections and proves the generated output is byte-
identical to the original v1.4 Markdown. It refuses duplicate IDs, mismatched
metadata, incorrect prompt count, unsafe paths or existing source-file overwrites.
After initialization, it validates rather than re-splitting and overwriting edits.

The old `library/healthcare_prompt_library_v1.4.md` and PDF remain historical v1.4
snapshots. The PDF is **not rebuilt** by this migration. Use the new compiled
Markdown and current contract for maintained content. Prompt IDs in the existing
human-readable metadata are validated, but this release does not certify every
historical YAML field as a portable machine schema; use the JSON manifest for routing.

## Deployment

Use a host's actual persistent-instruction, file-retrieval and execution facilities.
Do not assume one platform's upload path, UI, model list, context window or sampling
controls applies to another. A pasted prompt does not confer vendor-data access.

For OpenAI programmatic integrations, consult the current
[Responses migration documentation](https://platform.openai.com/docs/guides/migrate-to-responses)
and [deprecation register](https://platform.openai.com/docs/deprecations) rather
than the obsolete Assistants API guidance in historical documents. This repository
does not ship an API adapter or assert identical capabilities across hosts.

## Evaluation

[evaluations/cases.json](evaluations/cases.json) converts the four worked examples
into explicit review cases with scored dimensions and critical-failure rules.
Use [the protocol](evaluations/README.md) to retain actual inputs, outputs, model,
prompt commit and human grades. No model outputs have been generated or graded
as part of this packaging migration; these cases are a benchmark definition, not
an empirical claim of research quality. Build tests check integrity, not clinical
judgment or investment returns.

## Maintenance

A branch-restricted initialization workflow commits generated parts only to the
maintenance branch. Normal CI is read-only and checks current rebuild equality.
Do not publish private positions, expert-network records or licensed documents as
fixtures. Use synthetic or appropriately authorized material and keep sources
separate from instructions. MIT; see [LICENSE](LICENSE).
