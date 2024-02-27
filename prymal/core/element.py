"""Core HTML Functionality"""

from collections import defaultdict
from collections.abc import Callable, Iterable
from typing import Self, TypeAlias

from .style import Style
from .utils import AbstractHashable

ElementType: TypeAlias = "Element"


class Element(AbstractHashable):
    """
    Base element class from which all other elements derive from.
    """

    def __init__(self, style: Style = Style(), *children: ElementType) -> None:
        self.parent: ElementType = self
        self._children: list[Element] = []
        self.event_listeners: dict[str, list[Callable]] = defaultdict(list)
        self.style: Style = style
        self.style._elements.add(self)

    @property
    def children(self) -> Iterable[ElementType]:
        """
        Don't want to make it easy to erase all children.
        """
        return iter(self._children)

    def clear_children(self) -> None:
        self._children.clear()

    def add_event_listener(self) -> None:
        """Allows for adding event listeners such as on_hover or clicked"""
        ...

    def __call__(self, *children: ElementType) -> Self:
        """
        Used for adding children to the element.
        """
        self._children.extend(children)
        return self

    def clear_style(self) -> Self:
        self.style = Style()
        return self

    def __matmul__(self, style: Style) -> Self:
        self.style &= style
        return self

    def append_element(self, element: ElementType) -> None:
        self._children.append(element)

    def append_elements(self, *elements: ElementType) -> None:
        self._children.extend(elements)

    def __add__(self, other: ElementType) -> Self:
        self._children.append(other)
        other.parent = self
        return self

    def __iadd__(self, element: Self) -> None:
        self._children.append(element)
        element.parent = self

    def __render(self, pretty=True, indent=2) -> str:
        """
        Renders the element for web
        """
        ...
