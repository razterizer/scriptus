from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
import os

import bible as bib
import gutenberg as pg


def get_parser() -> ArgumentParser:
    parser = ArgumentParser(
        description='Loads the KJV project gutenberg bible, and saves it to plaintext files below a specified folder.',
        formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "filename", help="The file path to the project gutenberg bible"
    )
    parser.add_argument(
        "output", help="The path to the resulting output folder"
    )
    return parser


def save_book(book: bib.Book, filename: str) -> None:
    """Saves book in the file filename. The stored text will not include chapter numbers or verse numbers.
    The entire book is stored one verse per row in the file.

    Parameters
    ----------
    book: bible.Book
        The book object to be saved.
    filename
        The file name where to save the book.
    """
    with open(filename, 'w') as fp:
        verses = book.verses_book()
        for txt in verses:
            fp.write(f"{txt}\n")


def save_chapters(book: bib.Book, sub_folder: str):
    """Saves book under sub_folder, creates one file per chapter.
    Every row in the file is a verse.

    Parameters
    ----------
    book: bible.Book
        The book object to be saved.
    sub_folder: str
        The folder where to save all the chapters.
    """
    if not os.path.exists(sub_folder):
        os.makedirs(sub_folder)
    chapters = book.chapters()
    for ch in chapters:
        filename = os.path.join(sub_folder, ("%0*d" % (3, ch)) + ".txt")
        with open(filename, 'w') as fp:
            verses = book.verses_chapter(ch)
            for v in verses:
                fp.write(f"{v}\n")


def save_plaintext(bible: bib.Bible, folder_name: str):
    """Saves the bible object in plain text in directory folder_name.
    There are 2 main ways they are stored. The first is to store an entire book in plain text in a single file.
    There are no chapter numbers or verses, it's just a flat list of verses for the entire book.

    Parameters
    ----------
    bible
        _description_
    folder_name
        _description_
    """
    # if os.path.exists(folder_name):
    #     raise FileExistsError(f"ERROR: The folder \"{folder_name}\" already exists.\n")
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    n_books = bible.books()
    for i in range(n_books):
        sub_file = os.path.join(folder_name, ("%0*d" % (2, i + 1)) + ".txt")
        book = bible.book(i)
        save_book(book, sub_file)
        sub_folder = os.path.join(folder_name, ("%0*d" % (2, i + 1)))
        save_chapters(book, sub_folder)


def main():
    args = get_parser().parse_args()
    print(f"Loading {args.filename}")
    bible = pg.load(args.filename)
    print(f"Writing files to folder: {args.output}")
    save_plaintext(bible=bible, folder_name=args.output)


if __name__ == "__main__":
    main()
