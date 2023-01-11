from . import cbook
from ._enums import CapStyle, JoinStyle
from .path import Path
from .transforms import Affine2D, IdentityTransform, Transform

from numpy.typing import ArrayLike
from typing import Literal, Union

TICKLEFT: int
TICKRIGHT: int
TICKUP: int
TICKDOWN: int
CARETLEFT: int
CARETRIGHT: int
CARETUP: int
CARETDOWN: int
CARETLEFTBASE: int
CARETRIGHTBASE: int
CARETUPBASE: int
CARETDOWNBASE: int

class MarkerStyle:
    markers: dict[str | int, str]
    filled_markers: tuple[str, ...]
    fillstyles: tuple[FillStyleType, ...]
    def __init__(
        self,
        marker: str | ArrayLike | Path | MarkerStyle | None = ...,
        fillstyle: FillStyleType | None = ...,
        transform: Transform | None = ...,
        capstyle: CapStyle | None = ...,
        joinstyle: JoinStyle | None = ...,
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def is_filled(self) -> bool: ...
    def get_fillstyle(
        self,
    ) -> FillStyleType: ...
    def get_joinstyle(self) -> JoinStyle: ...
    def get_capstyle(self) -> CapStyle: ...
    def get_marker(self) -> str | ArrayLike | Path | MarkerStyle | None: ...
    def get_path(self) -> Path: ...
    def get_transform(self) -> Transform: ...
    def get_alt_path(self) -> Path: ...
    def get_alt_transform(self) -> Transform: ...
    def get_snap_threshold(self) -> float | None: ...
    def get_user_transform(self) -> Transform | None: ...
    def transformed(self, transform: Affine2D) -> MarkerStyle: ...
    def rotated(
        self, *, deg: float | None = ..., rad: float | None = ...
    ) -> MarkerStyle: ...
    def scaled(self, sx: float, sy: float | None = ...) -> MarkerStyle: ...

MarkerType = Union[str, Path, MarkerStyle]
FillStyleType = Literal["full", "left", "right", "bottom", "top", "none"]
