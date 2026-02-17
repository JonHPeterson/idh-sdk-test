from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourcesResponse")


@_attrs_define
class SourcesResponse:
    """Source details response

    Attributes:
        src_uuid (str):
        src_name (str):
        properties (Union[Unset, str]): Optional properties in JSON format
    """

    src_uuid: str
    src_name: str
    properties: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        src_uuid = self.src_uuid

        src_name = self.src_name

        properties = self.properties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "src_uuid": src_uuid,
                "src_name": src_name,
            }
        )
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        src_uuid = d.pop("src_uuid")

        src_name = d.pop("src_name")

        properties = d.pop("properties", UNSET)

        sources_response = cls(
            src_uuid=src_uuid,
            src_name=src_name,
            properties=properties,
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
