from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sources_response_fields import SourcesResponseFields


T = TypeVar("T", bound="SourcesResponse")


@_attrs_define
class SourcesResponse:
    """Source details response

    Attributes:
        src_uuid (str):
        src_name (str):
        fields (SourcesResponseFields): Map of fields as a set of name value pairs
    """

    src_uuid: str
    src_name: str
    fields: "SourcesResponseFields"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        src_uuid = self.src_uuid

        src_name = self.src_name

        fields = self.fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "src_uuid": src_uuid,
                "src_name": src_name,
                "fields": fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sources_response_fields import SourcesResponseFields

        d = dict(src_dict)
        src_uuid = d.pop("src_uuid")

        src_name = d.pop("src_name")

        fields = SourcesResponseFields.from_dict(d.pop("fields"))

        sources_response = cls(
            src_uuid=src_uuid,
            src_name=src_name,
            fields=fields,
        )

        sources_response.additional_properties = d
        return sources_response

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
