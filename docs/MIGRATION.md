# Migration: healthcare-first v2 to all-sector v3

The active project is now **Full Sector Research Agent v3.0.0**, with equal first-class coverage of all eleven major equity sectors. This is not the earlier healthcare pack plus a general template.

The repository remains `HHFinAi/healthcare-equity-prompt-library`; its private visibility, ownership, MIT license and Git history are unchanged. No repository deletion or force-push is needed. The previous v2 commit is `58bfdfabaa8928e5e7565125b4a74fc8d8498211`, preserved by `archive/healthcare-first-agent-v2-2026-09-24`.

The original v1.4 collection remains under `reference/` and at `archive/prompt-library-v1.4-2026-09-24`, whose starting commit is `fcf07f395c0993a1bea1c01539cc2cd8e63fb892`. These archives are supplementary historical material, not governing instructions; old platform/model guidance may be outdated.

V3 moves active sector definitions to `sector_agent/sector_data.py` and adds explicit single/multi/all routing, 79 custom research subsectors, sector-scoped specialist calls, twelve workflows, new equity/NAV methods and evidence-scope controls. Earlier single-healthcare briefs remain supported when their subsector ID exists in the new catalog; the active default template is now all-sector. A generic `general` sector is no longer accepted as a substitute for real sector coverage.

Restore through a reviewed revert or a normal descendant commit built from the archive tree. Do not force-reset shared history. Archived v2 outputs remain labeled v2 and are not retrospectively validated by v3 tests.
