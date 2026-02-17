from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TSGetTagInfoResponse")


@_attrs_define
class TSGetTagInfoResponse:
    """Timeseries tag info response

    Attributes:
        tag_uuid (str):
        source_uuid (str):
        source_data_uuid (str):
        data_type (int):
        uom (str):
        record_count (int):
        earliest_time_iso8601 (str):
        latest_time_iso8601 (str):
    """

    tag_uuid: str
    source_uuid: str
    source_data_uuid: str
    data_type: int
    uom: str
    record_count: int
    earliest_time_iso8601: str
    latest_time_iso8601: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag_uuid = self.tag_uuid

        source_uuid = self.source_uuid

        source_data_uuid = self.source_data_uuid

        data_type = self.data_type

        uom = self.uom

        record_count = self.record_count

        earliest_time_iso8601 = self.earliest_time_iso8601

        latest_time_iso8601 = self.latest_time_iso8601

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tag_uuid": tag_uuid,
                "source_uuid": source_uuid,
                "source_data_uuid": source_data_uuid,
                "data_type": data_type,
                "uom": uom,
                "record_count": record_count,
                "earliest_time_iso8601": earliest_time_iso8601,
                "latest_time_iso8601": latest_time_iso8601,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tag_uuid = d.pop("tag_uuid")

        source_uuid = d.pop("source_uuid")

        source_data_uuid = d.pop("source_data_uuid")

        data_type = d.pop("data_type")

        uom = d.pop("uom")

        record_count = d.pop("record_count")

        earliest_time_iso8601 = d.pop("earliest_time_iso8601")

        latest_time_iso8601 = d.pop("latest_time_iso8601")

        ts_get_tag_info_response = cls(
            tag_uuid=tag_uuid,
            source_uuid=source_uuid,
            source_data_uuid=source_data_uuid,
            data_type=data_type,
            uom=uom,
            record_count=record_count,
            earliest_time_iso8601=earliest_time_iso8601,
            latest_time_iso8601=latest_time_iso8601,
        )

        ts_get_tag_info_response.additional_properties = d
        return ts_get_tag_info_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
