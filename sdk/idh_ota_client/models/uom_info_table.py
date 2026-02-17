from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="UOMInfoTable")


@_attrs_define
class UOMInfoTable:
    """
    Attributes:
        names (list[str]):
        plural_names (list[str]):
        symbols (list[str]):
        defs (list[str]):
        definitions (list[str]):
        comments (list[str]):
        is_base (list[bool]):
        is_dimensionless (list[bool]):
        aliases (list[str]):
    """

    names: list[str]
    plural_names: list[str]
    symbols: list[str]
    defs: list[str]
    definitions: list[str]
    comments: list[str]
    is_base: list[bool]
    is_dimensionless: list[bool]
    aliases: list[str]

    def to_dict(self) -> dict[str, Any]:
        names = self.names

        plural_names = self.plural_names

        symbols = self.symbols

        defs = self.defs

        definitions = self.definitions

        comments = self.comments

        is_base = self.is_base

        is_dimensionless = self.is_dimensionless

        aliases = self.aliases

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "names": names,
                "plural_names": plural_names,
                "symbols": symbols,
                "defs": defs,
                "definitions": definitions,
                "comments": comments,
                "is_base": is_base,
                "is_dimensionless": is_dimensionless,
                "aliases": aliases,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        names = cast(list[str], d.pop("names"))

        plural_names = cast(list[str], d.pop("plural_names"))

        symbols = cast(list[str], d.pop("symbols"))

        defs = cast(list[str], d.pop("defs"))

        definitions = cast(list[str], d.pop("definitions"))

        comments = cast(list[str], d.pop("comments"))

        is_base = cast(list[bool], d.pop("is_base"))

        is_dimensionless = cast(list[bool], d.pop("is_dimensionless"))

        aliases = cast(list[str], d.pop("aliases"))

        uom_info_table = cls(
            names=names,
            plural_names=plural_names,
            symbols=symbols,
            defs=defs,
            definitions=definitions,
            comments=comments,
            is_base=is_base,
            is_dimensionless=is_dimensionless,
            aliases=aliases,
        )

        return uom_info_table
