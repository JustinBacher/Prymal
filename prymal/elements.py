from typing import Self

from .core.element import Element, ElementType
from .core.style import Style


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

    def __init__(self) -> None:
        super().__init__()
        super().__init__()
