from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VersionInfoResponse")


@_attrs_define
class VersionInfoResponse:
    """Version information response

    Attributes:
        version (str):
        build_time (str):
        git_commit (str):
        lib_c_version (str):
    """

    version: str
    build_time: str
    git_commit: str
    lib_c_version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        build_time = self.build_time

        git_commit = self.git_commit

        lib_c_version = self.lib_c_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "buildTime": build_time,
                "gitCommit": git_commit,
                "libCVersion": lib_c_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("version")

        build_time = d.pop("buildTime")

        git_commit = d.pop("gitCommit")

        lib_c_version = d.pop("libCVersion")

        version_info_response = cls(
            version=version,
            build_time=build_time,
            git_commit=git_commit,
            lib_c_version=lib_c_version,
        )

        version_info_response.additional_properties = d
        return version_info_response

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
