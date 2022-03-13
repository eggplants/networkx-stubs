from collections.abc import Generator
from typing import Any, NamedTuple

def not_implemented_for(*graph_types): ...
def open_file(path_arg, mode: str = ...): ...
def nodes_or_number(which_args): ...
def preserve_random_state(func) -> Generator[None, None, Any]: ...
def np_random_state(random_state_argument): ...
def random_state(random_state_argument): ...
def py_random_state(random_state_argument): ...

class argmap:
    def __init__(self, func, *args, try_finally: bool = ...) -> None: ...
    def __call__(self, f): ...
    def compile(self, f): ...
    def assemble(self, f): ...
    @classmethod
    def signature(cls, f): ...

    class Signature(NamedTuple):
        name: Any
        signature: Any
        def_sig: Any
        call_sig: Any
        names: Any
        n_positional: Any
        args: Any
        kwargs: Any
