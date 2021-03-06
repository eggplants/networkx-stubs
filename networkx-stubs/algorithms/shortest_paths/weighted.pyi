from collections.abc import Generator
from typing import Any

def dijkstra_path(G, source, target, weight: str = ...): ...
def dijkstra_path_length(G, source, target, weight: str = ...): ...
def single_source_dijkstra_path(
    G, source, cutoff: Any | None = ..., weight: str = ...
): ...
def single_source_dijkstra_path_length(
    G, source, cutoff: Any | None = ..., weight: str = ...
): ...
def single_source_dijkstra(
    G, source, target: Any | None = ..., cutoff: Any | None = ..., weight: str = ...
): ...
def multi_source_dijkstra_path(
    G, sources, cutoff: Any | None = ..., weight: str = ...
): ...
def multi_source_dijkstra_path_length(
    G, sources, cutoff: Any | None = ..., weight: str = ...
): ...
def multi_source_dijkstra(
    G, sources, target: Any | None = ..., cutoff: Any | None = ..., weight: str = ...
): ...
def dijkstra_predecessor_and_distance(
    G, source, cutoff: Any | None = ..., weight: str = ...
): ...
def all_pairs_dijkstra(
    G, cutoff: Any | None = ..., weight: str = ...
) -> Generator[Any, None, None]: ...
def all_pairs_dijkstra_path_length(
    G, cutoff: Any | None = ..., weight: str = ...
) -> Generator[Any, None, None]: ...
def all_pairs_dijkstra_path(
    G, cutoff: Any | None = ..., weight: str = ...
) -> Generator[Any, None, None]: ...
def bellman_ford_predecessor_and_distance(
    G, source, target: Any | None = ..., weight: str = ..., heuristic: bool = ...
): ...
def bellman_ford_path(G, source, target, weight: str = ...): ...
def bellman_ford_path_length(G, source, target, weight: str = ...): ...
def single_source_bellman_ford_path(G, source, weight: str = ...): ...
def single_source_bellman_ford_path_length(G, source, weight: str = ...): ...
def single_source_bellman_ford(
    G, source, target: Any | None = ..., weight: str = ...
): ...
def all_pairs_bellman_ford_path_length(
    G, weight: str = ...
) -> Generator[Any, None, None]: ...
def all_pairs_bellman_ford_path(G, weight: str = ...) -> Generator[Any, None, None]: ...
def goldberg_radzik(G, source, weight: str = ...): ...
def negative_edge_cycle(G, weight: str = ..., heuristic: bool = ...): ...
def find_negative_cycle(G, source, weight: str = ...): ...
def bidirectional_dijkstra(G, source, target, weight: str = ...): ...
def johnson(G, weight: str = ...): ...
