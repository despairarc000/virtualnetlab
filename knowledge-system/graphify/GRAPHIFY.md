# Graphify — dependency and evidence graph
Status: ACTIVE bootstrap | 2026-10-23.

## Purpose
Offer navigable edges between Markdown documentation and Python source/test import relationships so agents can answer: Where is this required? What depends on this? Which evidence/decision/test might be affected?

## Generate
`python tools/knowledge.py graph` prints generated Markdown node/edge report.
`python tools/knowledge.py graph --output knowledge-system/graphify/RELATIONSHIPS.md` writes a reproducible snapshot when needed (commit after review).
`python tools/knowledge.py doctor` verifies internal markdown links, required canonical files and reachable vault pages.

## Semantics
- `doc-link`: explicit relative Markdown reference.
- `python-import`: static import dependency between known local Python modules; conservative, no dynamic import guessing.
- future edges: `requirement->implementation`, `implementation->test`, `decision->source` must be authored as explicit links or validated graph metadata before advertised.
- Graphify is not invented semantic knowledge. Mark unresolved or speculative relations as PROPOSED in vault documents.
- Avoid recursion through massive irrelevant modules; navigate immediate neighbors as needed.

## Limitations
Initial parser ignores dynamic imports, wiki links, advanced GitHub reference links, and HTML tags; linked local .md pages + Python import graph are supported. This is an MVP knowledge tool and should expand with tests, not broad claims.
