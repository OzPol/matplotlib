from matplotlib.axes._base import _AxesBase
from matplotlib.axis import Axis, Tick

from matplotlib.colors import Color
from matplotlib.transforms import Transform

from typing import Literal, Callable, Iterable
from numpy.typing import ArrayLike

class SecondaryAxis(_AxesBase):
    def __init__(
        self,
        parent: _AxesBase,
        orientation: Literal["x", "y"],
        location: Literal["top", "bottom", "right", "left"] | float,
        functions: tuple[
            Callable[[ArrayLike], ArrayLike], Callable[[ArrayLike], ArrayLike]
        ]
        | Transform,
        **kwargs
    ) -> None: ...
    def set_alignment(
        self, align: Literal["top", "bottom", "right", "left"]
    ) -> None: ...
    def set_location(
        self, location: Literal["top", "bottom", "right", "left"] | float
    ) -> None: ...
    def set_ticks(
        self,
        ticks: Iterable[float],
        labels: Iterable[str] | None = ...,
        *,
        minor: bool = ...,
        **kwargs
    ) -> list[Tick]: ...
    def set_functions(
        self,
        functions: tuple[
            Callable[[ArrayLike], ArrayLike], Callable[[ArrayLike], ArrayLike]
        ]
        | Transform,
    ): ...
    def set_aspect(self, *args, **kwargs) -> None: ...
    def set_color(self, color: Color) -> None: ...
