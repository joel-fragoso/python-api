from src.domain.exceptions import InvalidCategoryException


class CategoryName:
    def __init__(self, value: str) -> None:
        if not value or len(value) > 45:
            raise InvalidCategoryException()
        self.__value = value

    @property
    def value(self) -> str:
        return self.__value
