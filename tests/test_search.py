import unittest
from src.directory import Directory
from src.file import File
from src.filter_by_size import FilterBySize


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.files: list[File] = []
        self.directory_1: Directory = Directory("directory_1")
        self.directory_2: Directory = Directory("directory_2")
        self.directory_1.add_child(self.directory_2)
        self.directory_3: Directory = Directory("directory_3")
        self.directory_2.add_child(self.directory_3)

        for i in range(3):
            self.files.append(File(f'file_1{i+1}.txt', 200*(i+1), 'txt'))
            self.directory_1.add_child(self.files[-1])

        for i in range(2):
            self.files.append(File(f'file_2{i+1}.txt', 300*(i+1), 'txt'))
            self.directory_2.add_child(self.files[-1])

        self.files.append(File(f'file_31.py', 1000, 'py'))
        self.directory_3.add_child(self.files[-1])
        self.files.append(File(f'file_11.py', 1000, 'py'))
        self.directory_3.add_child(self.files[-1])

    def test_filter_by_size(self):
        filter_1: FilterBySize = FilterBySize(1000)
        filter_2: FilterBySize = FilterBySize(600)

        files: list[File] = self.directory_1.search([filter_2])
        self.assertEqual(len(files), 1)
        self.assertEqual(files[0].name, "file_13.txt")

        files = self.directory_1.search([filter_2], True)
        self.assertEqual(len(files), 2)
        self.assertTrue(files[0].name == 'file_22.txt')

        files = self.directory_1.search([filter_1])
        self.assertEqual(len(files), 0)
        files = self.directory_1.search([filter_1], True)
        self.assertEqual(len(files), 2)


if __name__ == "__main__":
    unittest.main()
