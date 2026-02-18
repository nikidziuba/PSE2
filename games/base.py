from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Protocol


@dataclass
class SaveLocation:
    label: str
    path: Path


class GamePlugin(Protocol):
    id: str
    name: str

    def get_default_locations(self) -> List[SaveLocation]:
        ...

    def get_es3_key(self) -> str:
        ...

    def parse_save(self, raw: Dict[str, Any]) -> Dict[str, Any]:
        ...

    def serialize_save(self, structured: Dict[str, Any]) -> Dict[str, Any]:
        ...
