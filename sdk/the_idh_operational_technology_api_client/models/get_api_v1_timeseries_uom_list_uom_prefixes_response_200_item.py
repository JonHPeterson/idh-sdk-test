from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiV1TimeseriesUomListUomPrefixesResponse200Item")


@_attrs_define
class GetApiV1TimeseriesUomListUomPrefixesResponse200Item:
    """
    Attributes:
        name (Union[Unset, str]):
        symbol (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    symbol: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        symbol = self.symbol

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        symbol = d.pop("symbol", UNSET)

        value = d.pop("value", UNSET)

        get_api_v1_timeseries_uom_list_uom_prefixes_response_200_item = cls(
            name=name,
            symbol=symbol,
            value=value,
        )

        get_api_v1_timeseries_uom_list_uom_prefixes_response_200_item.additional_properties = d
        return get_api_v1_timeseries_uom_list_uom_prefixes_response_200_item

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
