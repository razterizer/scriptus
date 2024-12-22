from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from typing import List

from nltk.tokenize import word_tokenize


def get_parser() -> ArgumentParser:
    parser = ArgumentParser(
        description='Loads plaintext bible file, converts it, removes comma and punctuation, and saves the result.',
        formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "filename", help="The file path to the plain text bible."
    )
    parser.add_argument(
        "results", help="The file path of the results."
    )
    return parser


def save_flattened(words: List[str], filename: str) -> None:
    n = len(words)
    i = 0
    with open(filename, "w") as fp:
        for w in words:
            fp.write(w)
            if i + 1 < n:
                fp.write(" ")
            i += 1


def main() -> None:
    args = get_parser().parse_args()
    print(f"Loading and processing {args.filename}")

    with open(args.filename, 'r') as fp:
        lines = fp.readlines()

    # NOTE: '\'s' removes a postfix of a word, maybe not ideal, but this is just a test anyway
    reject = set([',', ';', ':', '.', '!', '?', '\'', '\'s', '(', ')', '-', '--', '+', '*', '/', ''])
    flat_word_list = []
    for cur_line in lines:
        tok = word_tokenize(cur_line)
        for w in tok:
            if w not in reject:
                flat_word_list.append(w.lower())

    print(f"Saving {args.results}")
    save_flattened(words=flat_word_list, filename=args.results)


if __name__ == "__main__":
    main()
