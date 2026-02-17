from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ts_sample_array_info import TSSampleArrayInfo


T = TypeVar("T", bound="GetSamplesResult")


@_attrs_define
class GetSamplesResult:
    """
    Attributes:
        is_status (list[bool]):
        timestamps_ns (list[int]):
        array_info (TSSampleArrayInfo):
        values (Union[Unset, list[float]]):
        values_str (Union[Unset, list[str]]):
    """

    is_status: list[bool]
    timestamps_ns: list[int]
    array_info: "TSSampleArrayInfo"
    values: Union[Unset, list[float]] = UNSET
    values_str: Union[Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_status = self.is_status

        timestamps_ns = self.timestamps_ns

        array_info = self.array_info.to_dict()

        values: Union[Unset, list[float]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        values_str: Union[Unset, list[str]] = UNSET
        if not isinstance(self.values_str, Unset):
            values_str = self.values_str

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "is_status": is_status,
                "timestamps_ns": timestamps_ns,
                "array_info": array_info,
            }
        )
        if values is not UNSET:
            field_dict["values"] = values
        if values_str is not UNSET:
            field_dict["values_str"] = values_str

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ts_sample_array_info import TSSampleArrayInfo

        d = dict(src_dict)
        is_status = cast(list[bool], d.pop("is_status"))

        timestamps_ns = cast(list[int], d.pop("timestamps_ns"))

        array_info = TSSampleArrayInfo.from_dict(d.pop("array_info"))

        values = cast(list[float], d.pop("values", UNSET))

        values_str = cast(list[str], d.pop("values_str", UNSET))

        get_samples_result = cls(
            is_status=is_status,
            timestamps_ns=timestamps_ns,
            array_info=array_info,
            values=values,
            values_str=values_str,
        )

        return get_samples_result
