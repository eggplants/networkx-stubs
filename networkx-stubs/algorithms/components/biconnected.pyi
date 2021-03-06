from collections.abc import Generator
from typing import Any

def is_biconnected(G): ...
def biconnected_component_edges(G) -> None: ...
def biconnected_components(G) -> Generator[Any, None, None]: ...
def articulation_points(G) -> Generator[Any, None, None]: ...
