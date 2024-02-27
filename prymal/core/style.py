"""
Core Styling Functionality
"""

from typing import Any, Self, TypeAlias

from .element import ElementType
from .utils import AbstractHashable

StyleType: TypeAlias = "Style"


class Style(AbstractHashable):
    """
    Provides an ease and flexible way of applying style attributes to elements
    without the need for handling selectors. It functions similarly to a
    CSS style class, allowing you to specify style properties without the
    requirement for naming conventions found in other frameworks.

    Styles can be combined using the union `&` or `&=` operators to create new
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

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self._elements: set[ElementType] = set()
        self.properties: list[Any] = []

    def copy(self) -> StyleType:
        new_style = super(self.__class__)
        new_style.properties = self.properties.copy()
        return new_style

    def __copy__(self) -> StyleType:
        return self.copy()

    def __and__(self, other_style: StyleType) -> StyleType:
        """
        Combines two styles together

        Example:

        ```py
        Style("red") & Style(flex_direction = "horizontal")
        ```
        """
        new_style = self.copy()
        new_style.properties += other_style.properties
        return new_style

    def __iand__(self, other_style: StyleType) -> Self:
        self.properties += other_style.properties
        return self
