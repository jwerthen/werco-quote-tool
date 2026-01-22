# Coding Standards

This document defines the initial code quality standards for QuoteEngine.

## General

- Keep changes focused and small.
- Favor explicit over implicit behavior.
- Add or update tests for new behavior.

## Python (Backend)

- Target Python 3.11.
- Use type hints for public functions.
- Prefer Pydantic models for request/response schemas.
- Keep modules small and single-purpose.

## TypeScript (Frontend)

- Use functional components.
- Keep state localized unless shared.
- Prefer explicit types for props and API responses.
