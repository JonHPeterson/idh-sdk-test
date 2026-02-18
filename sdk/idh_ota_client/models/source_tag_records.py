from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.source_tag_record import SourceTagRecord


T = TypeVar("T", bound="SourceTagRecords")


@_attrs_define
class SourceTagRecords:
    """Object containing array of source tag records

    Attributes:
        source_tags (list['SourceTagRecord']): Array of source tag records
    """

    source_tags: list["SourceTagRecord"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_tags = []
        for source_tags_item_data in self.source_tags:
            source_tags_item = source_tags_item_data.to_dict()
            source_tags.append(source_tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_tags": source_tags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_tag_record import SourceTagRecord

        d = dict(src_dict)
        source_tags = []
        _source_tags = d.pop("source_tags")
        for source_tags_item_data in _source_tags:
            source_tags_item = SourceTagRecord.from_dict(source_tags_item_data)

            source_tags.append(source_tags_item)

        source_tag_records = cls(
            source_tags=source_tags,
        )

        source_tag_records.additional_properties = d
        return source_tag_records

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
