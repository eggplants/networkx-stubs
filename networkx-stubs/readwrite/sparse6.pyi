from collections.abc import Generator
from typing import Any

def from_sparse6_bytes(string) -> Generator[None, None, Any]: ...
def to_sparse6_bytes(G, nodes: Any | None = ..., header: bool = ...): ...
def read_sparse6(path): ...
def write_sparse6(G, path, nodes: Any | None = ..., header: bool = ...) -> None: ...
