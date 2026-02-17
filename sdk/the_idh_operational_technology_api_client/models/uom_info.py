from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UOMInfo")


@_attrs_define
class UOMInfo:
    """
    Attributes:
        name (str):
        plural_name (str):
        symbol (str):
        def_ (str):
        definition (str):
        comment (str):
        is_base (bool):
        is_dimensionless (bool):
        aliases (str): comma-separated list of aliases for the UOM
    """

    name: str
    plural_name: str
    symbol: str
    def_: str
    definition: str
    comment: str
    is_base: bool
    is_dimensionless: bool
    aliases: str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        plural_name = self.plural_name

        symbol = self.symbol

        def_ = self.def_

        definition = self.definition

        comment = self.comment

        is_base = self.is_base

        is_dimensionless = self.is_dimensionless

        aliases = self.aliases

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "plural_name": plural_name,
                "symbol": symbol,
                "def": def_,
                "definition": definition,
                "comment": comment,
                "is_base": is_base,
                "is_dimensionless": is_dimensionless,
                "aliases": aliases,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        plural_name = d.pop("plural_name")

        symbol = d.pop("symbol")

        def_ = d.pop("def")

        definition = d.pop("definition")

        comment = d.pop("comment")

        is_base = d.pop("is_base")

        is_dimensionless = d.pop("is_dimensionless")

        aliases = d.pop("aliases")

        uom_info = cls(
            name=name,
            plural_name=plural_name,
            symbol=symbol,
            def_=def_,
            definition=definition,
            comment=comment,
            is_base=is_base,
            is_dimensionless=is_dimensionless,
            aliases=aliases,
        )

        return uom_info
