from __future__ import annotations

from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

from backend.app.core.config import settings


class LocalFileStorage:
    def __init__(self, root: Path | None = None) -> None:
        self.root = root or Path(settings.storage_path)
        self.root.mkdir(parents=True, exist_ok=True)

    def save(self, file: UploadFile) -> tuple[str, Path]:
        file_id = uuid4().hex
        destination = self.root / f"{file_id}_{file.filename}"
        with destination.open("wb") as handle:
            for chunk in iter(lambda: file.file.read(1024 * 1024), b""):
                handle.write(chunk)
        return file_id, destination
