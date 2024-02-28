"""
Built-in Styles
"""

from enum import Enum
from typing import Generic, TypeAlias, TypeVar

from .core import Style, StyleProperty

T = TypeVar("T", int | float)
Vector3Type: TypeAlias = "Vector3" 

class Vector3(Generic[T]):
    def __init__(self, x: T, y: T, z: T, \, min: T, max: T) -> None:
        if (min <= x <= max) or (min <= y <= max) or (min <= z <= max):
            raise ValueError(f"Values for {self.__class__} must be between {min} and {max} inclusively")

        self._x: T = x
        self._y: T = y
        self._z: T = z

    def __vec(self) -> tuple[T, T, T]:
        return (self._x, self._y, self._z)

    def __hash__(self) -> int:
        return hash(self.__vec)
        
    def __eq__(self, other: Vector3Type) -> bool:
        if isinstance(other, other: Vector3Type):
            return self.__vec == other.__vec
        return False
        
    def __repr__(self) -> str:
        return f"{self.__class__.lower()}({x}, {y}, {z})"

class Vector4(Generic[T]):
    def __init__(self, x: T, y: T, z: T, a : int, \, min: T, max: T) -> None:
        if (min <= x <= max) or (min <= y <= max) or (min <= z <= max):
            raise ValueError(f"Values for {self.__class__} must be between {min} and {max} inclusively")

        if 0 <= a <= 100:
            raise ValueError("Alpha must be between 0 and 100 inclusively")

        self._x: T = x
        self._y: T = y
        self._z: T = z
        self._a: int = a

    def __vec(self) -> tuple[T, T, T]:
        return (self._x, self._y, self._z, self._a)

    def __hash__(self) -> int:
        return hash(self.__vec)
        
    def __eq__(self, other: Vector3Type) -> bool:
        if isinstance(other, other: Vector3Type):
            return self.__vec == other.__vec
        return False
        
    def __repr__(self) -> str:
        return f"{self.__class__.lower()}({self._x}, {self._y}, {self._z}, {self._a})"


class RGB(Vector3):
    def __init__(self, red: int, green: int, blue: int, alpha: int = 100) -> None:
        super().__init__(red, green, blue, alpha, 0, 255)

    @property
    def red(self) -> int:
        return self._x

    @property
    def green(self) -> int:
        return self._y

    @property
    def blue(self) -> int:
        return self._z

    @property
    def alpha(self) -> int:
        return self._a


"""
Text Styling
"""

class TextDecoration(Enum):
    Bold = StyleProperty("text_decoration", "bold")
    Italic = StyleProperty("text_decoration", "italic")
    Underline = StyleProperty("text_decoration", "underline")
    StrikeThrough = StyleProperty("text_decoration", "bold")

class Color:
  
