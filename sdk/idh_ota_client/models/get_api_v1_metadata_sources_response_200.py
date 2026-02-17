from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sources_response import SourcesResponse


T = TypeVar("T", bound="GetApiV1MetadataSourcesResponse200")


@_attrs_define
class GetApiV1MetadataSourcesResponse200:
    """ """

    additional_properties: dict[str, "SourcesResponse"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sources_response import SourcesResponse

        d = dict(src_dict)
        get_api_v1_metadata_sources_response_200 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = SourcesResponse.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        get_api_v1_metadata_sources_response_200.additional_properties = additional_properties
        return get_api_v1_metadata_sources_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "SourcesResponse":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "SourcesResponse") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
