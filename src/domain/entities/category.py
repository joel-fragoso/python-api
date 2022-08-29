# pylint: disable=invalid-name
from src.domain.value_object import CategoryId, CategoryName


class Category:
    # pylint: disable=redefined-builtin
    def __init__(self, id: CategoryId, name: CategoryName) -> None:
        self.__id = id
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id.value

    @property
    def name(self) -> str:
        return self.__name.value
