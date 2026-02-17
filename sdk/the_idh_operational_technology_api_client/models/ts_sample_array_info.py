from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.time_series_sample import TimeSeriesSample


T = TypeVar("T", bound="TSSampleArrayInfo")


@_attrs_define
class TSSampleArrayInfo:
    """
    Attributes:
        tag_uuid (str):
        data_type (int):
        uom (str):
        sample_count (int):
        start_boundary (TimeSeriesSample):
        end_boundary (TimeSeriesSample):
        data_assembly_time (float):
    """

    tag_uuid: str
    data_type: int
    uom: str
    sample_count: int
    start_boundary: "TimeSeriesSample"
    end_boundary: "TimeSeriesSample"
    data_assembly_time: float

    def to_dict(self) -> dict[str, Any]:
        tag_uuid = self.tag_uuid

        data_type = self.data_type

        uom = self.uom

        sample_count = self.sample_count

        start_boundary = self.start_boundary.to_dict()

        end_boundary = self.end_boundary.to_dict()

        data_assembly_time = self.data_assembly_time

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tag_uuid": tag_uuid,
                "data_type": data_type,
                "uom": uom,
                "sample_count": sample_count,
                "start_boundary": start_boundary,
                "end_boundary": end_boundary,
                "data_assembly_time": data_assembly_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.time_series_sample import TimeSeriesSample

        d = dict(src_dict)
        tag_uuid = d.pop("tag_uuid")

        data_type = d.pop("data_type")

        uom = d.pop("uom")

        sample_count = d.pop("sample_count")

        start_boundary = TimeSeriesSample.from_dict(d.pop("start_boundary"))

        end_boundary = TimeSeriesSample.from_dict(d.pop("end_boundary"))

        data_assembly_time = d.pop("data_assembly_time")

        ts_sample_array_info = cls(
            tag_uuid=tag_uuid,
            data_type=data_type,
            uom=uom,
            sample_count=sample_count,
            start_boundary=start_boundary,
            end_boundary=end_boundary,
            data_assembly_time=data_assembly_time,
        )

        return ts_sample_array_info
