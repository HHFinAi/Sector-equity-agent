# Migration: healthcare-first v2 to all-sector v3

The active project is now **Full Sector Research Agent v3.0.0**, with equal first-class coverage of all eleven major equity sectors. This is not the earlier healthcare pack plus a general template.

The active public repository is [HHFinAi/Sector-equity-agent](https://github.com/HHFinAi/Sector-equity-agent). At the original migration, the recorded repository name was `HHFinAi/healthcare-equity-prompt-library` and its visibility was private. Those details describe the migration baseline, not the current repository identity or visibility. No repository deletion or force-push is needed. The migration recorded the previous v2 commit as `a930aa93ce4ff04318070f2cb8c2b92543fa7407`, preserved by `archive/healthcare-first-agent-v2-2026-09-24`.

The original v1.4 collection remains under `reference/` and at `archive/prompt-library-v1.4-2026-09-24`, whose starting commit is `8de2ea45a89451209ee1ad03dcfba00c468dbf4c`. These archives are supplementary historical material, not governing instructions; old platform/model guidance may be outdated.

V3 moves active sector definitions to `sector_agent/sector_data.py` and adds explicit single/multi/all routing, 79 custom research subsectors, sector-scoped specialist calls, twelve workflows, new equity/NAV methods and evidence-scope controls. Earlier single-healthcare briefs remain supported when their subsector ID exists in the new catalog; the active default template is now all-sector. A generic `general` sector is no longer accepted as a substitute for real sector coverage.

Restore through a reviewed revert or a normal descendant commit built from the archive tree. Do not force-reset shared history. Archived v2 outputs remain labeled v2 and are not retrospectively validated by v3 tests.
