from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTestPage")


@attr.s(auto_attribs=True)
class GetTestPage:
    """
    Attributes:
        page_start (Union[Unset, int]):  Example: 1.
        page_limit (Union[Unset, int]):  Default: 25.
    """

    page_start: Union[Unset, int] = UNSET
    page_limit: Union[Unset, int] = 25
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        page_start = self.page_start
        page_limit = self.page_limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_start is not UNSET:
            field_dict["page.start"] = page_start
        if page_limit is not UNSET:
            field_dict["page.limit"] = page_limit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        page_start = d.pop("page.start", UNSET)

        page_limit = d.pop("page.limit", UNSET)

        get_test_page = cls(
            page_start=page_start,
            page_limit=page_limit,
        )

        get_test_page.additional_properties = d
        return get_test_page

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
