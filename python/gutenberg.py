import re

import bible as bib


def load(filename: str) -> bib.Bible:
    """Loads project gutenberg bible in this repo

    Parameters
    ----------
    filename: str
        The file path to the gutenberg file

    Returns
    -------
        bible.Bible: A Bible object containing the text
    """
    bible: bib.Bible = bib.Bible()
    title_read: bool = False
    count_empty_lines: int = 0
    chapter: int = 0
    verse: int = 0
    cur_book: bib.Book | None = None
    re_comp = re.compile(r"(\d+):(\d+)")
    with open(filename, encoding="utf-8-sig", newline="\n") as fp:
        for line in fp:
            line = line.strip()
            if line == "":
                count_empty_lines += 1
                continue
            if not title_read:
                bible.set_name(name=line)
                title_read = True
                count_empty_lines = 0
                continue
            if count_empty_lines > 3:
                # Here we have a title of a book (except title for the new testament)
                if line != "The New Testament of the King James Bible":
                    if cur_book is not None:
                        bible.add_book(book=cur_book)
                    cur_book = bib.Book(name=line)
                    chapter = 0
                    verse = 0
            else:
                assert cur_book is not None
                # Handling different cases of "chapter:verse TEXT HERE", "TEXT chapter:verse MORE TEXT", etc
                matches = re_comp.finditer(line)
                match = None
                prev_pos = 0
                for match in matches:
                    cur_pos = match.start()
                    prepend = line[prev_pos : cur_pos].strip()
                    if prepend != "":
                        cur_book.add_verse(chapter, verse, prepend)
                    chapter = int(match.groups()[0])
                    verse = int(match.groups()[1])
                    prev_pos = match.end()
                if match is not None or chapter != 0:
                    postpend = line[prev_pos:].strip()
                    if postpend != "":
                        cur_book.add_verse(chapter, verse, postpend)
                else:
                    # This case is when we get to i.e. "Otherwise Called:" on book names
                    name = cur_book.name()
                    if name != "":
                        name += (", " if line[-1] == ":" else " ")
                    name += line
                    cur_book.set_name(name)

            count_empty_lines = 0
        bible.add_book(book=cur_book)
    return bible
