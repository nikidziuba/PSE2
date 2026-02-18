from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict
import json

from es3_modifier import ES3


@dataclass
class ES3Backend:
    key: str
    _original_data: bytes = field(default=b"", init=False)

    def load_bytes(self, data: bytes) -> Dict[str, Any]:
        
        self._original_data = data
        es3 = ES3(data, self.key)
        return es3.load()

    def save_bytes(self, payload: Dict[str, Any]) -> bytes:
        if not self._original_data:
            raise RuntimeError("No original data loaded before save.")
        es3 = ES3(self._original_data, self.key)
        raw_json = json.dumps(payload)
        return es3.save(raw_json)

    def load_from_file(self, path: Path) -> Dict[str, Any]:
        if not path.is_file():
            raise FileNotFoundError(f"Save file not found: {path}")
        data = path.read_bytes()
        return self.load_bytes(data)

    def save_to_file(self, path: Path, payload: Dict[str, Any]) -> None:
        if path.exists():
            backup_name = f"{path.name}.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
            backup_path = path.with_name(backup_name)
            backup_path.write_bytes(path.read_bytes())

        data = self.save_bytes(payload)
        path.write_bytes(data)
