from __future__ import annotations

from backend.app.schemas.extraction import ExtractionResult


class ExtractionStore:
    _records: dict[str, ExtractionResult] = {}

    def save(self, result: ExtractionResult) -> ExtractionResult:
        self._records[result.file_id] = result
        return result

    def get(self, file_id: str) -> ExtractionResult | None:
        return self._records.get(file_id)
