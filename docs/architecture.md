# Architecture Overview

This document is a placeholder for the QuoteEngine system architecture. It will evolve alongside the implementation.

## Layers

- **Client layer**: Web UI (React) for uploads, extraction review, and quoting.
- **API layer**: FastAPI backend exposing file, quote, routing, and pricing endpoints.
- **Processing layer**: Parsers, feature extraction, routing rules, and cost calculation engines.
- **Data layer**: PostgreSQL for persistence, Redis for cache/queue, object storage for files.

## Next Steps

- Define concrete service boundaries and module layout.
- Map data flows between parsing, routing, costing, and document generation.
- Document deployment topology for dev and production.
