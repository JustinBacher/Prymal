"""
Core Styling Functionality
"""

from types import UnionType
from typing import Any, Self, TypeAlias

from .elements import BaseElement

StyleType: TypeAlias = "Style"


class Style:
    """
    Provides an ease and flexible way of applying style attributes to elements
    without the need for handling selectors. It functions similarly to a
    CSS style class, allowing you to specify style properties without the
    requirement for naming conventions found in other frameworks.

    Styles can be combined using the union `|` or `|=` operators to create new
    styles. They can be reused even if they are combined because combining
    them creates a whole new style to avoid conflicts.

    Applying a function to an element is as simple as using the `@` or `@=`
    operators.

    Example usage:

    ```py
    emphasis = Style(font_style="bold")

    Container()(
        Text("Hello World!") @ emphasis
    ) @ Style(flex_direction = "horizontal")
    ```
    """

    def __init__(self, **kwargs: Any) -> None:
        self.selectors: list[str] = []
        self.properties: list[Any] = []

    def copy(self) -> StyleType:
        new_style = super(self.__class__)
        new_style.selectors = self.selectors.copy()
        new_style.properties = self.properties.copy()
        return new_style

    def __or__(self, other_style: Any) -> StyleType:
        """Combines two styles together"""
        new_style = self.copy()
        new_style.selectors += other_style.selectors
        new_style.properties += other_style.properties
        return new_style

    __ior__ = __or__
