from typing import Any

def could_be_isomorphic(G1, G2): ...

graph_could_be_isomorphic = could_be_isomorphic

def fast_could_be_isomorphic(G1, G2): ...

fast_graph_could_be_isomorphic = fast_could_be_isomorphic

def faster_could_be_isomorphic(G1, G2): ...

faster_graph_could_be_isomorphic = faster_could_be_isomorphic

def is_isomorphic(
    G1, G2, node_match: Any | None = ..., edge_match: Any | None = ...
): ...
