# QuoteEngine Build Task List

Ordered task checklist derived from `overview.md` to guide implementation from repo setup through Phase 3 delivery.

## 0. Project Setup & Governance
- [x] Initialize repository structure (`backend/`, `frontend/`, `infra/`, `docs/`, `scripts/`).
- [x] Add basic documentation: README, architecture overview, contributing guide.
- [x] Define coding standards (linting, formatting, commit conventions).
- [x] Configure CI (tests, lint, type checks) and pre-commit hooks.
- [ ] Establish issue tracking labels and milestones aligned to phases.

## 1. Core Engine (MVP) — Phase 1 Weeks 1–12

### 1.1 File Parsing (Weeks 1–4)
- [x] Create backend service skeleton (FastAPI app, config, dependency injection).
- [x] Define core data models for extraction results and geometry primitives.
- [x] Implement file upload API and storage (local or S3-compatible).
- [ ] Implement STEP parser (PythonOCC):
  - [ ] Bounding box extraction.
  - [ ] Volume and surface area extraction.
  - [ ] Unit detection.
  - [ ] Hole detection (basic).
- [ ] Implement DXF parser (ezdxf + shapely):
  - [ ] Bounding rectangle.
  - [ ] Cut length.
  - [ ] Pierce count.
  - [ ] Hole detection (circles/arcs).
  - [ ] Layer analysis.
- [ ] Add PDF parsing scaffold (pdfplumber/pypdf) for metadata extraction.
- [x] Implement extraction result persistence and API response schema.
- [ ] Create parser unit tests with fixtures.

### 1.2 Routing & Costing (Weeks 5–8)
- [ ] Implement rule engine framework for process routing.
- [ ] Define routing rule schema and seed baseline rules (saw, drill, weld, blast, paint).
- [ ] Implement time calculation formulas per operation.
- [ ] Implement material cost calculator.
- [ ] Implement labor cost calculator (with burdened rates).
- [ ] Implement consumables calculator (weld wire, gas, abrasives).
- [ ] Create routing + costing API endpoints.
- [ ] Add routing/costing unit tests.

### 1.3 Output & UI (Weeks 9–12)
- [ ] Create quote data model and database schema (PostgreSQL).
- [ ] Build quote CRUD APIs (create, retrieve, update, list).
- [ ] Implement simple web UI (upload, extraction review, quote summary).
- [ ] Implement PDF quote generation.
- [ ] Implement internal review document generation.
- [ ] Add integration tests for full quote workflow.

## 2. Intelligence — Phase 2 Weeks 13–22

### 2.1 Advanced Extraction (Weeks 13–16)
- [ ] Implement structural shape detection (W, C, L, HSS).
- [ ] Implement weld length estimation between bodies.
- [ ] Implement bend line detection for DXF (layer conventions).
- [ ] Implement complexity scoring.
- [ ] Implement full PDF drawing parsing (text, dimensions, tolerances).
- [ ] Expand extraction validation and confidence scoring.

### 2.2 Smart Routing (Weeks 17–20)
- [ ] Expand routing rule library (thickness/material-specific).
- [ ] Implement thickness-based routing adjustments.
- [ ] Implement material-specific routing adjustments.
- [ ] Implement similar part matching (vector similarity store).
- [ ] Add learning/feedback loop from actuals (accuracy tracking).

### 2.3 Enhanced UI (Weeks 21–22)
- [ ] Implement 3D STEP viewer (three.js).
- [ ] Implement 2D DXF viewer (canvas/Fabric.js).
- [ ] Implement routing editor (reorder, edit times).
- [ ] Implement manual override workflow and audit trail.

## 3. Integration — Phase 3 Weeks 23–30

### 3.1 External Integrations (Weeks 23–26)
- [ ] Build ERP integration API framework.
- [ ] Integrate material pricing API.
- [ ] Implement customer portal (quote requests).

### 3.2 Analytics & Optimization (Weeks 27–30)
- [ ] Implement quote win/loss tracking.
- [ ] Build accuracy analytics dashboard.
- [ ] Implement margin optimization suggestions.
- [ ] Implement lead time forecasting.

## 4. Infrastructure & DevOps
- [ ] Dockerize backend and frontend.
- [ ] Define Docker Compose setup for dev (Postgres, Redis, MinIO).
- [ ] Add Celery workers and Redis broker.
- [ ] Configure production deployment targets (Kubernetes manifests or Terraform).
- [ ] Add monitoring (Prometheus, Grafana) and structured logging.

## 5. Testing & Validation
- [ ] Implement unit tests for all parsers and calculators.
- [ ] Build integration tests for full quote workflow.
- [ ] Build accuracy test suite with fixture CAD files.
- [ ] Add load/performance tests (file parsing, routing, quoting).
- [ ] Define acceptance criteria per phase and execute validation reports.

## 6. Documentation & Training
- [ ] Write API reference docs (OpenAPI + examples).
- [ ] Document system architecture and data flows.
- [ ] Create user onboarding guide for estimators.
- [ ] Create admin guide for materials, labor rates, and rules.
