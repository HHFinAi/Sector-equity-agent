# Migration from prompt library v1.4

The active project is now **Sector Research Agent v2.0.0**. The repository remains `HHFinAi/healthcare-equity-prompt-library`, and the migration does not change its private visibility or account ownership.

The original main-branch commit before replacement is:

```text
fcf07f395c0993a1bea1c01539cc2cd8e63fb892
```

The original prompt collection, PDF, standing instructions, worked examples, README and changelog are preserved under `reference/`, with original file contents and the MIT license retained. The old root `.DS_Store` is intentionally omitted. The archive is supplementary historical material: platform/model recommendations in it may be outdated and are not governing instructions for the new runtime.

The migration adds the executable Python workflow, prompt contracts, six workflow definitions, healthcare/general sector packs, deterministic valuation helpers, synthetic examples, tests, documentation and local review controls. It does not claim that the 113 archived prompts have individually become autonomous tools. They are reusable research references; the nine new specialist stages govern execution.

## Reversibility

A normal descendant commit replaces the active file tree; no force-push or history deletion is required. The original commit remains reachable through Git history. An `archive/prompt-library-v1.4-2026-09-24` branch is created at the original commit as an additional recovery pointer. Restore with a reviewed revert or a new commit based on the original tree, rather than force-resetting shared history.
