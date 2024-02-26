"""
Component class and implementation
"""

from .style import Style

_base_style = Style()


class Component:
    """Outlines the functionality of a Prymal Component"""

    def __init__(self, style: Style = _base_style) -> None:
        self.style = style
