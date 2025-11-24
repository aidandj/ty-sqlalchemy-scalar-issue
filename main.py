from dataclasses import dataclass
from typing import Any, Generic, Tuple, Type, TypeVar, assert_type


@dataclass
class User: ...


_T = TypeVar("_T", bound=Any)
_TP = TypeVar("_TP", bound=Tuple[Any, ...])


class Select(Generic[_TP]): ...


def _select1(typ: Type[_T]) -> Select[Tuple[_T]]:
    return Select()


def _select2(typ: Type[_T]) -> Tuple[_T]:
    return (typ(),)


assert_type(_select1(User), Select[Tuple[User]])
assert_type(_select2(User), Tuple[User])
