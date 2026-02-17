from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ParseUOMResult")


@_attrs_define
class ParseUOMResult:
    """
    Attributes:
        name (str):
        symbol (str):
        def_ (str):
    """

    name: str
    symbol: str
    def_: str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        symbol = self.symbol

        def_ = self.def_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "symbol": symbol,
                "def": def_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        symbol = d.pop("symbol")

        def_ = d.pop("def")

        parse_uom_result = cls(
            name=name,
            symbol=symbol,
            def_=def_,
        )

        return parse_uom_result
