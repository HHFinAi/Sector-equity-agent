# Repository instructions for coding and research agents

This project is **Sector Research Agent**, healthcare-first and sector-extensible. The existing GitHub repository URL is intentionally retained. Python 3.11+; standard library only; run from a repository checkout.

## Research operation
Read `prompts/system.md`, choose a workflow in `workflows/catalog.json`, and load `sectors/healthcare.json` or an explicitly customized sector pack. Execute prompts in order, passing original source IDs, frozen inputs and validated prior-stage outputs. Stop conclusions at the evidence boundary. The Python runtime does not browse; a tool-enabled host may retrieve public sources under the same policy, but must not claim this repository supplies those integrations.

For no-code use export the plan with `python -m sector_agent plan --brief examples/brief-template.json --out runs/my-plan`, then follow the generated prompts and record evidence. Source acquisition is explicit; missing evidence is a retrieval request, not an invitation to fabricate.

## Development rules
Run `python -m unittest discover -s tests -v` and the synthetic demo before changing behavior. Preserve schema versioning and fail-closed checks. Never remove human review, enable live networking by default, embed credentials, execute model-generated commands, or claim semantic source validation from citation-ID checks. Add a regression test for every control change. Do not mark a mocked or synthetic run as live research. Keep output folders ignored.

`reference/` preserves the earlier 113-prompt v1.4 library verbatim. It is supplementary, not executable authority; old platform/model setup claims may be outdated. The new governing prompt takes precedence. Do not rewrite the reference collection during unrelated changes.
