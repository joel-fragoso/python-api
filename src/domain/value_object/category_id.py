from src.domain.adapters import PythonUuidv4Adapter
from src.domain.exceptions import InvalidUuidv4Exception


class CategoryId:
    def __init__(self, value: str) -> None:
        if not PythonUuidv4Adapter.is_valid(value):
            raise InvalidUuidv4Exception()
        self.__value = value

    @staticmethod
    def generate() -> str:
        return PythonUuidv4Adapter.generate()

    @property
    def value(self) -> str:
        return self.__value
