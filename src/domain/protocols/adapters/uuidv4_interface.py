from abc import ABCMeta, abstractmethod


class Uuidv4AdapterInterface(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def generate() -> str:
        pass

    @staticmethod
    @abstractmethod
    def is_valid(value: str) -> bool:
        pass
