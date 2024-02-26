"""
Events are things that can happen to an Element, such as being clicked,
hovered, or gaining or losing focus.
"""

from __future__ import annotations

from enum import IntEnum, auto
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


class EventType(IntEnum):
    Client = auto()
    Server = auto()


class BaseEvent:
    """
    Base event from which all other events are derived from.
    """

    ...


def event(
    f: Callable[P, T],
    event_type: EventType = EventType.Server,
) -> Callable[P, T]:
    """
    An event can either be in Python or another language.
    """

    @wraps(f)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        return f(*args, **kwargs)

    return wrapper
