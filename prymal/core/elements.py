"""Core HTML Functionality"""

from collections import defaultdict
from collections.abc import Callable
from typing import Self, TypeAlias

from .style import Style

BASE_STYLE = Style()
BaseElementType: TypeAlias = "BaseElement"


class BaseElement:
    """
    Base element class from which all other elements derive from.
    """

    def __init__(self, style: Style = BASE_STYLE) -> None:
        self._parent: BaseElementType = self
        self.children: list[BaseElement] = []
        self.style: Style = style
        self.event_listeners: dict[str, list[Callable]] = defaultdict(list)

    @property
    def parent(self) -> BaseElementType:
        return self._parent

    @parent.setter
    def parent(self, parent: BaseElementType) -> None:
        if self.parent:
            raise ValueError("Cannot reassign element after assignment")

        self._parent = parent

    def add_event_listener(self) -> None:
        """Allows for adding event listeners such as on_hover or clicked"""
        ...

    def __call__(self, *children: BaseElementType) -> BaseElementType:
        """
        Used for adding children to the element.
        """
        self.children.extend(children)
        return self

    def __matmul__(self, other: Style) -> Self:
        self.style |= other
        return self


class Container(BaseElement):
    """
    The most fundamental element for grouping or organizing elements in a user
    interface. The `Container` is a box to seamlessly group and style UI elements
    together.

    Functionally equivalent to a `<div>` in HTML, `UIView` in iOS, or a `View`
    in Android.
    """

    def __init__(self, style: Style | None = None, *children: BaseElement) -> None:
        super().__init__()
        for element in children:
            element.parent = self
        self.children: list[BaseElementType] = list(children)

    def __iadd__(self, element: Self) -> None:
        self.children.append(element)
        element.parent = self


class Text(BaseElement):
    """
    Display rich text supporting styling and interactivity.
    """

    def __init__(self, *text: str) -> None:
        super().__init__()
        self.text = text


class TextInput(BaseElement):
    """
    Element for retrieving text from the user.
    """

    def __init__(
        self,
    ) -> None:
        super().__init__()
        super().__init__()
