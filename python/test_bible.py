import pytest

import python.bible as bib


def test_empty_bible():
    """
    TYPE test:

    """
    bible = bib.Bible()
    assert "" == bible.name()
    assert 0 == bible.books()


def test_empty_book():
    book = bib.Book()
    assert "" == book.name()
    assert [] == book.chapters()
    with pytest.raises(Exception) as exc:
        book.verse(1, 1)
    assert "" != str(exc.value)
    with pytest.raises(Exception) as exc:
        book.verse_indices(1)
    assert "" != str(exc.value)


def test_add_empty_verse():
    """
    TYPE test:

    """
    book = bib.Book()
    book.add_verse(3, 1, "")
    book.add_verse(3, 4, "")
    assert [3] == book.chapters()
    assert [1, 4] == book.verse_indices(3)
    assert book.verse(3, 1) == ""
    assert book.verse(3, 4) == ""
    with pytest.raises(Exception):
        book.verse_indices(1)
    with pytest.raises(Exception):
        book.verse_indices(4)

    bible = bib.Bible()
    bible.add_book(book)
    assert bible.name() == ""
    assert bible.books() == 1


def test_add_some_verse():
    """
    TYPE test:

    """
    book = bib.Book()
    book.add_verse(31, 7, "A")
    book.add_verse(13, 4, "B")
    assert "A" == book.verse(31, 7)
    assert "B" == book.verse(13, 4)
    assert [13, 31] == book.chapters()


def test_add_some_verses():
    """
    TYPE test:

    """
    book = bib.Book()
    book.add_verse(31, 7, "A")
    book.add_verse(13, 4, "B")
    book.add_verse(13, 1, "C")
    assert ["C", "B"] == book.verses_chapter(13)
    assert ["C", "B", "A"] == book.verses_book()
