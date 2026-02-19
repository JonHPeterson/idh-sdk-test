from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ts_get_tag_info_response import TSGetTagInfoResponse


T = TypeVar("T", bound="GetAllTagInfoResponse200")


@_attrs_define
class GetAllTagInfoResponse200:
    """ """

    additional_properties: dict[str, list["TSGetTagInfoResponse"]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for componentsschemas_ts_get_tag_info_responses_item_data in prop:
                componentsschemas_ts_get_tag_info_responses_item = (
                    componentsschemas_ts_get_tag_info_responses_item_data.to_dict()
                )
                field_dict[prop_name].append(componentsschemas_ts_get_tag_info_responses_item)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ts_get_tag_info_response import TSGetTagInfoResponse

        d = dict(src_dict)
        get_all_tag_info_response_200 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for componentsschemas_ts_get_tag_info_responses_item_data in _additional_property:
                componentsschemas_ts_get_tag_info_responses_item = TSGetTagInfoResponse.from_dict(
                    componentsschemas_ts_get_tag_info_responses_item_data
                )

                additional_property.append(componentsschemas_ts_get_tag_info_responses_item)

            additional_properties[prop_name] = additional_property

        get_all_tag_info_response_200.additional_properties = additional_properties
        return get_all_tag_info_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list["TSGetTagInfoResponse"]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list["TSGetTagInfoResponse"]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
