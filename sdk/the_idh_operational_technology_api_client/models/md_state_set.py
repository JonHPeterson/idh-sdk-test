from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.md_state_set_states import MDStateSetStates


T = TypeVar("T", bound="MDStateSet")


@_attrs_define
class MDStateSet:
    """State set details

    Attributes:
        src_uuid (str):
        state_set_id (int):
        state_set_name (str):
        states (MDStateSetStates): Mapping of state IDs to names
    """

    src_uuid: str
    state_set_id: int
    state_set_name: str
    states: "MDStateSetStates"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        src_uuid = self.src_uuid

        state_set_id = self.state_set_id

        state_set_name = self.state_set_name

        states = self.states.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "src_uuid": src_uuid,
                "state_set_id": state_set_id,
                "state_set_name": state_set_name,
                "states": states,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.md_state_set_states import MDStateSetStates

        d = dict(src_dict)
        src_uuid = d.pop("src_uuid")

        state_set_id = d.pop("state_set_id")

        state_set_name = d.pop("state_set_name")

        states = MDStateSetStates.from_dict(d.pop("states"))

        md_state_set = cls(
            src_uuid=src_uuid,
            state_set_id=state_set_id,
            state_set_name=state_set_name,
            states=states,
        )

        md_state_set.additional_properties = d
        return md_state_set

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
