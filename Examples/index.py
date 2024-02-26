"""
Basic Example usage of Prymal

NOTE: This document is currently in draft form. It will be updated
substantially as Prymal is being developed.
"""

from pryml.core.elements import Container, Text
from pryml.core.style import Style

example = Container(style=Style(flex_direction="horizontal"))(
    Text("Hello World!") @ Style(font_style="bold"),
)
