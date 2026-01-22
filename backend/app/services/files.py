from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


@dataclass(slots=True)
class FileRecord:
    file_id: str
    filename: str
    status: str
    storage_path: Path
    created_at: datetime


class FileRepository:
    _records: dict[str, FileRecord] = {}

    def create(self, *, file_id: str, filename: str, status: str, storage_path: Path) -> FileRecord:
        record = FileRecord(
            file_id=file_id,
            filename=filename,
            status=status,
            storage_path=storage_path,
            created_at=datetime.now(timezone.utc),
        )
        self._records[file_id] = record
        return record

    def get(self, file_id: str) -> FileRecord | None:
        return self._records.get(file_id)
