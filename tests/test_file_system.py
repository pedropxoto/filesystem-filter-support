import unittest
from src.file import File
from src.directory import Directory


class TestFileSystem(unittest.TestCase):

    def test_file_initialization(self):
        file_name = "file.txt"
        file_size = 1200
        file_extension = "txt"
        file: File = File(file_name, file_size, file_name.split('.')[-1])

        self.assertEqual(file.name, file_name)
        self.assertEqual(file.size, file_size)
        self.assertEqual(file.type, file_extension)

    def test_directory_initialization(self):
        directory_name = "directory"
        directory: Directory = Directory(directory_name)

        self.assertEqual(directory.name, directory_name)

    def test_file_system(self):
        directory_name = "directory"
        directory: Directory = Directory(directory_name)

        file_name = "file.txt"
        file_size = 1200
        file: File = File(file_name, file_size, file_name.split('.')[-1])
        directory.add_child(file)

        self.assertEqual(len(directory.children), 1)


if __name__ == '__main__':
    unittest.main()
