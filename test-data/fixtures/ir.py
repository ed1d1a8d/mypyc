# These builtins stubs are used implicitly in AST to IR generation
# test cases.

from typing import (
    TypeVar, Generic, List, Iterator, Iterable, Sized, Dict, Optional, Tuple, Any,
    overload, Mapping, Union
)

T = TypeVar('T')
S = TypeVar('S')
K = TypeVar('K') # for keys in mapping
V = TypeVar('V') # for values in mapping

class object:
    def __init__(self) -> None: pass
    def __eq__(self, x: object) -> bool: pass
    def __ne__(self, x: object) -> bool: pass

class type:
    def __init__(self, o: object) -> None: ...

class ellipsis: pass

# Primitive types are special in generated code.

class int:
    def __init__(self, x: object, base: int = 10) -> None: pass
    def __add__(self, n: int) -> int: pass
    def __sub__(self, n: int) -> int: pass
    def __mul__(self, n: int) -> int: pass
    def __floordiv__(self, x: int) -> int: pass
    def __mod__(self, x: int) -> int: pass
    def __neg__(self) -> int: pass
    def __pos__(self) -> int: pass
    def __eq__(self, n: object) -> bool: pass
    def __ne__(self, n: object) -> bool: pass
    def __lt__(self, n: int) -> bool: pass
    def __gt__(self, n: int) -> bool: pass
    def __le__(self, n: int) -> bool: pass
    def __ge__(self, n: int) -> bool: pass

class str:
    def __init__(self, x: object) -> None: pass
    def __add__(self, x: str) -> str: pass
    def __eq__(self, x: object) -> bool: pass
    def __ne__(self, x: object) -> bool: pass
    def join(self, x: Iterable[str]) -> str: pass

class float:
    def __init__(self, x: object) -> None: pass
    def __add__(self, n: float) -> float: pass
    def __sub__(self, n: float) -> float: pass
    def __mul__(self, n: float) -> float: pass
    def __div__(self, n: float) -> float: pass

class bytes:
    def __init__(self, x: object) -> None: pass
    def __add__(self, x: object) -> bytes: pass
    def __eq__(self, x:object) -> bool:pass
    def __ne__(self, x: object) -> bool: pass
    def join(self, x: Iterable[object]) -> bytes: pass

class bool: pass

class tuple(Generic[T], Sized):
    def __init__(self, i: Iterable[T]) -> None: pass
    def __getitem__(self, i: int) -> T: pass
    def __len__(self) -> int: pass

class function: pass

class list(Generic[T], Iterable[T], Sized):
    def __init__(self, i: Optional[Iterable[T]] = None) -> None: pass
    def __getitem__(self, i: int) -> T: pass
    def __setitem__(self, i: int, o: T) -> None: pass
    def __delitem__(self, i: int) -> None: pass
    def __mul__(self, i: int) -> List[T]: pass
    def __rmul__(self, i: int) -> List[T]: pass
    def __iter__(self) -> Iterator[T]: pass
    def __len__(self) -> int: pass
    def append(self, x: T) -> None: pass
    def pop(self) -> T: pass
    def extend(self, l: Iterable[T]) -> None: pass
    def insert(self, i: int, x: T) -> None: pass
    def sort(self) -> None: pass

class dict(Mapping[K, V]):
    def __getitem__(self, key: K) -> V: pass
    def __setitem__(self, k: K, v: V) -> None: pass
    def __delitem__(self, k: K) -> None: pass
    def __contains__(self, item: object) -> bool: pass
    def __iter__(self) -> Iterator[K]: pass
    def __len__(self) -> int: pass
    def update(self, a: Mapping[K, V]) -> None: pass
    def pop(self, x: int) -> K: pass
    def keys(self) -> List[K]: pass

class set(Generic[T]):
    def __init__(self, i: Optional[Iterable[T]] = None) -> None: pass
    def __iter__(self) -> Iterator[T]: pass
    def __len__(self) -> int: pass
    def add(self, x: T) -> None: pass
    def remove(self, x: T) -> None: pass
    def discard(self, x: T) -> None: pass
    def clear(self) -> None: pass
    def pop(self) -> T: pass

class slice: pass

class BaseException: pass

class Exception(BaseException):
    def __init__(self, message: Optional[str] = None) -> None: pass

class AttributeError(Exception): pass

class LookupError(Exception): pass

class KeyError(LookupError): pass

class IndexError(LookupError): pass


def id(o: object) -> int: pass
def len(o: Sized) -> int: pass
def print(*object) -> None: pass
def range(x: int) -> Iterator[int]: pass
def isinstance(x: object, t: object) -> bool: pass
