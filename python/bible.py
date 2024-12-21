from functools import reduce
import operator
from typing import Dict, List


class Book:
    def __init__(self, name: str = "") -> None:
        self._name: str = name
        self._content: Dict[int, Dict[int, str]] = {}

    def name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def add_verse(self, chapter: int, verse: int, text: str, sep: str = " ") -> None:
        """Stores, or adds text to a verse.

        Parameters
        ----------
        chapter: int
            The chapter where text belongs.
        verse: int
            The verse where text belongs.
        text: str
            The verse text.
        sep: str, optional, default = " "
            Separator to add, assuming text already exists for this chapter and verse.

        Raises
        -------
            ValueError: For invalid argument input values.
        """
        if chapter <= 0 or verse <= 0:
            raise ValueError("chapter and/or verse are not valid with non-positive values.")
        if chapter not in self._content:
            self._content[chapter] = {}
        if verse not in self._content[chapter]:
            self._content[chapter][verse] = text
        else:
            self._content[chapter][verse] += sep + text

    def verse(self, chapter: int, verse: int) -> str:
        """Retrieves a verse, given a chapter and verse number.

        Parameters
        ----------
        chapter: int
            The specified chapter number.
        verse: int
            The specified verse number.

        Returns
        -------
            The specified verse text.
        """
        return self._content[chapter][verse]

    def chapters(self) -> List[int]:
        """Retuns a sorted list of chapters contained in this book.

        Returns
        -------
            List[int]: The chapter indices for this book.
        """
        ret = [x for x in self._content]
        ret.sort()
        return ret

    def verse_indices(self, chapter: int) -> List[int]:
        """Returns a sorted list of verse indices for a specified chapter.

        Parameters
        ----------
        chapter: int
            The specified chapter.

        Returns
        -------
            List[int]: The verse indices, given the chapter.
        """
        ret = [x for x in self._content[chapter]]
        ret.sort()
        return ret

    def verses_chapter(self, chapter: int) -> List[str]:
        """Returns the list of verse texts, given the chapter.

        Parameters
        ----------
        chapter: int
            The specified chapter.

        Returns
        -------
            List[str]: The verse texts for the specified chapter. One entry per verse.
        """
        vi = self.verse_indices(chapter)
        ret = [self.verse(chapter, i) for i in vi]
        return ret

    def verses_book(self) -> List[str]:
        """Returns the list of verse texts, for the entire book.

        Returns
        -------
            List[str]: The verse texts for the entire book. One entry per verse.
        """
        ch = self.chapters()
        all_verses = [self.verses_chapter(c) for c in ch]
        return list(reduce(operator.concat, all_verses))


class Bible:
    def __init__(self):
        self._name: str = ""
        self._books: List[Book] = []

    def set_name(self, name: str) -> None:
        self._name = name

    def name(self) -> str:
        return self._name

    def add_book(self, book: Book | None) -> None:
        if book is not None:
            self._books.append(book)

    def book(self, index: int) -> Book:
        return self._books[index]

    def books(self) -> int:
        return len(self._books)
