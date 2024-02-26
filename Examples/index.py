"""
Basic Example usage of Prymal

NOTE: This document is currently in draft form. It will be updated
substantially as Prymal is being developed.
"""

from prymal.core.elements import Container, Text
from prymal.core.style import Style

example = Container(style=Style(flex_direction="horizontal"))(
    Text("Hello World!") @ Style(font_style="bold"),
)
