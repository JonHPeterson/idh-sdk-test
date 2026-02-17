from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.asset_response_aliases import AssetResponseAliases
    from ..models.asset_response_properties import AssetResponseProperties


T = TypeVar("T", bound="AssetResponse")


@_attrs_define
class AssetResponse:
    """Asset details response

    Attributes:
        asset_uuid (str):
        asset_name (str):
        aliases (AssetResponseAliases): Mapping of alias names to UUIDs
        properties (AssetResponseProperties): Mapping of property names to values
        parent_assets (list[str]):
        child_assets (list[str]):
    """

    asset_uuid: str
    asset_name: str
    aliases: "AssetResponseAliases"
    properties: "AssetResponseProperties"
    parent_assets: list[str]
    child_assets: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_uuid = self.asset_uuid

        asset_name = self.asset_name

        aliases = self.aliases.to_dict()

        properties = self.properties.to_dict()

        parent_assets = self.parent_assets

        child_assets = self.child_assets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_uuid": asset_uuid,
                "asset_name": asset_name,
                "aliases": aliases,
                "properties": properties,
                "parent_assets": parent_assets,
                "child_assets": child_assets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_response_aliases import AssetResponseAliases
        from ..models.asset_response_properties import AssetResponseProperties

        d = dict(src_dict)
        asset_uuid = d.pop("asset_uuid")

        asset_name = d.pop("asset_name")

        aliases = AssetResponseAliases.from_dict(d.pop("aliases"))

        properties = AssetResponseProperties.from_dict(d.pop("properties"))

        parent_assets = cast(list[str], d.pop("parent_assets"))

        child_assets = cast(list[str], d.pop("child_assets"))

        asset_response = cls(
            asset_uuid=asset_uuid,
            asset_name=asset_name,
            aliases=aliases,
            properties=properties,
            parent_assets=parent_assets,
            child_assets=child_assets,
        )

        asset_response.additional_properties = d
        return asset_response

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
