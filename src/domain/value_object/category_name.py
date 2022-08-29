class CategoryName:
    def __init__(self, value: str) -> None:
        # if len(value) < 3:
        #     raise InvalidCategoryException()
        self.__value = value

    @property
    def value(self) -> str:
        return self.__value
