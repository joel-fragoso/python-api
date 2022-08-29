from .domain import DomainException


class InvalidCategoryException(DomainException):
    def __init__(self) -> None:
        super().__init__("A categoria é inválida")
