from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PrefixListResponse")


@_attrs_define
class PrefixListResponse:
    """Dictionary of arrays for UOM prefixes

    Attributes:
        prefix_name (list[str]): List of prefix names
        prefix_symbol (list[str]): List of prefix symbols
        prefix_factor (list[float]): List of prefix factors
    """

    prefix_name: list[str]
    prefix_symbol: list[str]
    prefix_factor: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prefix_name = self.prefix_name

        prefix_symbol = self.prefix_symbol

        prefix_factor = self.prefix_factor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prefix_name": prefix_name,
                "prefix_symbol": prefix_symbol,
                "prefix_factor": prefix_factor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prefix_name = cast(list[str], d.pop("prefix_name"))

        prefix_symbol = cast(list[str], d.pop("prefix_symbol"))

        prefix_factor = cast(list[float], d.pop("prefix_factor"))

        prefix_list_response = cls(
            prefix_name=prefix_name,
            prefix_symbol=prefix_symbol,
            prefix_factor=prefix_factor,
        )

        prefix_list_response.additional_properties = d
        return prefix_list_response

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
