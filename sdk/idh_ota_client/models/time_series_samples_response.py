from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.time_series_samples_response_data import TimeSeriesSamplesResponseData


T = TypeVar("T", bound="TimeSeriesSamplesResponse")


@_attrs_define
class TimeSeriesSamplesResponse:
    """
    Attributes:
        data (TimeSeriesSamplesResponseData):
    """

    data: "TimeSeriesSamplesResponseData"

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.time_series_samples_response_data import TimeSeriesSamplesResponseData

        d = dict(src_dict)
        data = TimeSeriesSamplesResponseData.from_dict(d.pop("data"))

        time_series_samples_response = cls(
            data=data,
        )

        return time_series_samples_response
