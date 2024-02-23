"""Core HTML Functionality"""

from csscore import Style


class HTMLElement:
    styles: list[Style] = []

    def __init__(self, self_closing: bool = False, **kwargs) -> None:
        self.self_closing = self_closing
        self.__dict__ |= kwargs

    def __repr__(self) -> str:
        name = self.__class__.__name__

        if self.self_closing:
            return f"<{name}/>"

        return f"<{name}>...</{name}>"
