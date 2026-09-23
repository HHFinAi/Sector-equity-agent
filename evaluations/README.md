# Human-graded regression protocol

Status: **NOT_RUN**. The four existing synthetic worked examples define test inputs
and reference patterns; they are not proof of model accuracy. A new model run must
be graded against the supplied facts, not against prose similarity to the example.

Record case ID, prompt commit, model/version, host/tools, run date, data cutoff,
complete input, raw output, source manifest and named reviewer. Grade each dimension
in `cases.json` from 0 to 4: 0 = materially wrong/absent; 1 = major problems;
2 = mixed/requires substantial correction; 3 = minor issues; 4 = fully supported
within the test's scope. Keep grading notes and disputed interpretations.

Proposed acceptance rule: every dimension at least 3 and no critical failure.
This is a release-policy choice, not an empirically calibrated investment metric.
Do not replace a failing numerical/source check with a high average score.
Compare revisions on the same frozen inputs. Expand the suite with adversarial
missing-consensus, conflicting-source and dilution cases before any stronger
production-readiness claim. No private or licensed research may be made public
merely to create a benchmark.
