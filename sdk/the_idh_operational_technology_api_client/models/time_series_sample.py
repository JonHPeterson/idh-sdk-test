from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeSeriesSample")


@_attrs_define
class TimeSeriesSample:
    """
    Attributes:
        is_status (bool):
        timestamp_ns (int):
        value (float):
        value_str (Union[Unset, str]):
    """

    is_status: bool
    timestamp_ns: int
    value: float
    value_str: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_status = self.is_status

        timestamp_ns = self.timestamp_ns

        value = self.value

        value_str = self.value_str

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "is_status": is_status,
                "timestamp_ns": timestamp_ns,
                "value": value,
            }
        )
        if value_str is not UNSET:
            field_dict["value_str"] = value_str

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_status = d.pop("is_status")

        timestamp_ns = d.pop("timestamp_ns")

        value = d.pop("value")

        value_str = d.pop("value_str", UNSET)

        time_series_sample = cls(
            is_status=is_status,
            timestamp_ns=timestamp_ns,
            value=value,
            value_str=value_str,
        )

        return time_series_sample
