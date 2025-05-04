from abc import ABC, abstractmethod
from src.file import File


class Filter(ABC):
    @abstractmethod
    def matches(self, file: File) -> bool:
        pass
