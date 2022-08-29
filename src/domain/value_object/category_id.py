class CategoryId:
    def __init__(self, value: str) -> None:
        self.__value = value

    @staticmethod
    def generate() -> str:
        return "category_id"

    @property
    def value(self) -> str:
        return self.__value
