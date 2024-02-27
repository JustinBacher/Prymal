from collections import defaultdict
from collections.abc import MutableSet
from threading import Lock
from types import NoneType
from typing import Callable, TypeVar

T = TypeVar("T")


class OrderedSet(defaultdict, MutableSet):
    """https://stackoverflow.com/questions/1653970/does-python-have-an-ordered-set"""

    def __init__(self, default_factory: Callable = NoneType) -> None:
        defaultdict.__init__(self, default_factory)
        MutableSet.__init__(self)

    def add(self, elem) -> None:
        self[elem]

    def discard(self, elem):
        self.pop(elem)

    def __le__(self, other):
        return all(e in other for e in self)

    def __lt__(self, other):
        return self <= other and self != other

    def __ge__(self, other):
        return all(e in self for e in other)

    def __gt__(self, other):
        return self >= other and self != other

    def __repr__(self):
        return f"OrderedSet([{", ".join(map(repr, self))}])"

    def __str__(self):
        return f"{", ".join(map(repr, self))}"

    difference = property(lambda self: self.__sub__)
    difference_update = property(lambda self: self.__isub__)
    intersection = property(lambda self: self.__and__)
    intersection_update = property(lambda self: self.__iand__)
    issubset = property(lambda self: self.__le__)
    issuperset = property(lambda self: self.__ge__)
    symmetric_difference = property(lambda self: self.__xor__)
    symmetric_difference_update = property(lambda self: self.__ixor__)
    union = property(lambda self: self.__or__)


class IDGenerator:
    __slots__ = ("lock", "_id")

    def __init__(self) -> None:
        self.lock = Lock()
        self._id = 0

    def __call__(self) -> int:
        with self.lock:
            self._id += 1
            return self._id


_id_generators = defaultdict(IDGenerator)


def generate_unique_id(key: str | type | None = None) -> int:
    """
    Used for generating unique IDs. Each key will use a different ID generator.
    """
    return _id_generators[key]()


class AbstractHashable:

    @property
    def id(self) -> int:
        try:
            self.__id
        except AttributeError:
            self.__id = generate_unique_id(self.__class__)

        return self.__id

    def __hash__(self) -> int:
        return self.id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.id == other.id
