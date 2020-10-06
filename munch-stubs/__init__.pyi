from typing import Any, Optional, Callable


class Munch(dict):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __getattr__(self, k: str) -> Any: ...
    def __setattr__(self, k: str, v: Any) -> None: ...
    def __delattr__(self, k: str) -> None: ...
    def toDict(self) -> dict: ...
    @property
    def __dict__(self): ...  # type: ignore
    def __dir__(self) -> list: ...
    __members__: Any = ...
    @classmethod
    def fromDict(cls, d: dict) -> "Munch": ...
    def copy(self) -> "Munch": ...
    def update(self, *args: Any, **kwargs: Any) -> None: ...
    def get(self, k: str, d: Optional[Any] = ...) -> Any: ...
    def setdefault(self, k: str, d: Optional[Any] = ...) -> Any: ...

class AutoMunch(Munch):
    def __setattr__(self, k: str, v: Any) -> None: ...

class DefaultMunch(Munch):
    __default__: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __getattr__(self, k: str) -> Any: ...
    def __setattr__(self, k: str, v: Any) -> None: ...
    def __getitem__(self, k: str) -> Any: ...
    @classmethod
    def fromDict(cls, d: dict, default: Optional[Any] = ...) -> "Munch": ...
    def copy(self) -> "Munch": ...

class DefaultFactoryMunch(Munch):
    default_factory: Callable[[],Any] = ...
    def __init__(self, default_factory: Callable[[],Any], *args: Any, **kwargs: Any) -> None: ...
    @classmethod
    def fromDict(cls, d: dict, default_factory: Callable[[],Any]) -> "Munch": ...  # type: ignore
    def copy(self) -> "Munch": ...
    def __setattr__(self, k: str, v: Any) -> None: ...
    def __missing__(self, k: str) -> Any: ...

def munchify(x: dict, factory: Any = ...) -> Munch: ...
def unmunchify(x: Munch) -> dict: ...
