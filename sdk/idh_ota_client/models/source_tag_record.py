from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.source_tag_record_properties import SourceTagRecordProperties


T = TypeVar("T", bound="SourceTagRecord")


@_attrs_define
class SourceTagRecord:
    """Source tag record

    Attributes:
        src_uuid (str):
        src_data_uuid (str):
        src_tag_name (str):
        properties (SourceTagRecordProperties): Map of properties as a set of name value pairs
    """

    src_uuid: str
    src_data_uuid: str
    src_tag_name: str
    properties: "SourceTagRecordProperties"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        src_uuid = self.src_uuid

        src_data_uuid = self.src_data_uuid

        src_tag_name = self.src_tag_name

        properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "src_uuid": src_uuid,
                "src_data_uuid": src_data_uuid,
                "src_tag_name": src_tag_name,
                "properties": properties,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_tag_record_properties import SourceTagRecordProperties

        d = dict(src_dict)
        src_uuid = d.pop("src_uuid")

        src_data_uuid = d.pop("src_data_uuid")

        src_tag_name = d.pop("src_tag_name")

        properties = SourceTagRecordProperties.from_dict(d.pop("properties"))

        source_tag_record = cls(
            src_uuid=src_uuid,
            src_data_uuid=src_data_uuid,
            src_tag_name=src_tag_name,
            properties=properties,
        )

        source_tag_record.additional_properties = d
        return source_tag_record

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
