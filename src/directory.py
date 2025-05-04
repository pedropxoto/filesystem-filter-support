from __future__ import annotations
from src.filter import Filter
from src.file import File


class Directory:
    name: str
    children: list[File | Directory]

    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add_child(self, item: File | Directory) -> None:
        self.children.append(item)

    def search(self, filters: list[Filter], recursive: bool = False) -> list[File]:

        files: list[File] = []

        for fs_item in self.children:
            if isinstance(fs_item, File) and self._is_file_valid(fs_item, filters):
                files.append(fs_item)
            if recursive and isinstance(fs_item, Directory):
                files.extend(fs_item.search(filters, recursive))

        return files

    @staticmethod
    def _is_file_valid(file: 'File', filters: list[Filter]):
        for filter_instance in filters:
            if not filter_instance.matches(file):
                return False
        return True
