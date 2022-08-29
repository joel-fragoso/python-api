from .domain import DomainException


class DuplicatedCategoryException(DomainException):
    def __init__(self) -> None:
        super().__init__("A categoria já está em uso")
