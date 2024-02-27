"""Core HTML Functionality"""

from collections import defaultdict
from collections.abc import Callable
from typing import Self, TypeAlias

from .style import Style
from .utils import AbstractHashable

ElementType: TypeAlias = "Element"


class Element(AbstractHashable):
    """
    Base element class from which all other elements derive from.
    """

    def __init__(self, style: Style = Style(), *children: ElementType) -> None:
        self._parent: ElementType = self
        self.children: list[Element] = []
        self.event_listeners: dict[str, list[Callable]] = defaultdict(list)
        self.style: Style = style
        self.style._elements.add(self)

    @property
    def parent(self) -> ElementType:
        return self._parent

    @parent.setter
    def parent(self, parent: ElementType) -> None:
        if self.parent:
            raise ValueError("Cannot reassign element after assignment")

        self._parent = parent

    def add_event_listener(self) -> None:
        """Allows for adding event listeners such as on_hover or clicked"""
        ...

    def __call__(self, *children: ElementType) -> Self:
        """
        Used for adding children to the element.
        """
        self.children.extend(children)
        return self

    def __matmul__(self, other_style: Style) -> Self:
        self.style &= other_style
        return self

    def __add__(self, other: ElementType) -> Self:
        self.children.append(other)
        other.parent = self
        return self

    def __iadd__(self, element: Self) -> None:
        self.children.append(element)
        element.parent = self


class Container(Element):
    """
    The most fundamental element for grouping or organizing elements in a user
    interface. The `Container` is a box to seamlessly group and style UI elements
    together.

    Functionally equivalent to a `<div>` in HTML, `UIView` in iOS, or a `View`
    in Android.
    """

    def __init__(self, style: Style | None = None, *children: Element) -> None:
        super().__init__()
        for element in children:
            element.parent = self
        self.children: list[ElementType] = list(children)

    def __iadd__(self, element: Self) -> None:
        self.children.append(element)
        element.parent = self


class Text(Element):
    """
    Display rich text supporting styling and interactivity.
    """

    def __init__(self, *text: str) -> None:
        super().__init__()
        self.text = text


class TextInput(Element):
    """
    Element for retrieving text from the user.
    """

    def __init__(
        self,
    ) -> None:
        super().__init__()
        super().__init__()
