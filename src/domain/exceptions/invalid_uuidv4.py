from .domain import DomainException


class InvalidUuidv4Exception(DomainException):
    def __init__(self) -> None:
        super().__init__("O uuid é inválido")
