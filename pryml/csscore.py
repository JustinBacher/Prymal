"""
Core CSS classes
"""

from typing import Iterable

from .component import Component
from .htmlcore import Tag


class Style:
    """A CSS style class"""

    def __init__(self, selectors: Iterable[str], properties: Iterable[str]) -> None:
        self.selectors = selectors
        self.properties = properties

    def __enter__(self, element: Tag | Component) -> None:
        element.styles.append(self)


class Property:
    """Defines a base CSS property"""

    def __init__(self) -> None:
        pass
