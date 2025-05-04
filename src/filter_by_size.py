from src.filter import Filter
from src.file import File


class FilterBySize(Filter):
    size: int

    def __init__(self, size: int):
        self.size = size

    def matches(self, file: File):
        return file.size == self.size
