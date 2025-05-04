# Filesystem Filter Support

This project is an implementation of a filter support for file and directory structures, enabling searches using customizable criteria such as file size, name, extension, etc.

## Class Structure

- `File`: Represents a file with attributes such as name and size.
- `Directory`: Represents a directory containing files and/or other directories.
- `Filter` (abstract): Interface for creating custom filters.
- `FilterBySize`: Filter that selects files based on size.

## Creating Custom Filters

The filtering system is designed to be easily extensible. To create a new filter, simply create a class that inherits from the abstract `Filter` class and implements the required method.

Each custom filter must implement the `matches(file: File) -> bool` method, which defines whether a given file satisfies the filter criteria.

## How Search Works

The `Directory` class contains the following method:

```python
search(filters: List[Filter], recursive: bool) -> List[File]
```

- `filters`: a list of filters implementing the `Filter` interface.
- `recursive`: if `True`, the search traverses subdirectories recursively.

## Usage Example

```python
dir = Directory("root")
file1 = File("a.txt", size=100, extension='txt')
file2 = File("b.txt", size=2000, extension='txt')
dir.add_child(file1)
dir.add_child(file2)

filter = FilterBySize(100)
results = dir.search([filter], recursive=False)

for file in results:
    print(file.name)
```