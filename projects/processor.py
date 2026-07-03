from pathlib import Path
from typing import Generator


class FileProcessor:
    """Utility class for common file operations."""

    def __init__(self, filepath: str):
        self.filepath = Path(filepath)

    def read(self) -> str:
        """Read the entire file."""
        try:
            with self.filepath.open("r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"{self.filepath} does not exist.")

    def read_lines(self) -> Generator[str, None, None]:
        """Yield one line at a time."""
        try:
            with self.filepath.open("r", encoding="utf-8") as file:
                for line in file:
                    yield line.strip()
        except FileNotFoundError:
            raise FileNotFoundError(f"{self.filepath} does not exist.")

    def write(self, text: str) -> None:
        """Overwrite the file."""
        with self.filepath.open("w", encoding="utf-8") as file:
            file.write(text)

    def append(self, text: str) -> None:
        """Append text to the file."""
        with self.filepath.open("a", encoding="utf-8") as file:
            file.write(text + "\n")

    def line_count(self) -> int:
        """Return total number of lines."""
        return sum(1 for _ in self.read_lines())

    def word_count(self) -> int:
        """Return total number of words."""
        return sum(len(line.split()) for line in self.read_lines())

    def search(self, keyword: str) -> list[str]:
        """Return lines containing the keyword."""
        return [
            line
            for line in self.read_lines()
            if keyword.lower() in line.lower()
        ]

    def copy_to(self, destination: str) -> None:
        """Copy contents to another file."""
        with open(destination, "w", encoding="utf-8") as dest:
            for line in self.read_lines():
                dest.write(line + "\n")