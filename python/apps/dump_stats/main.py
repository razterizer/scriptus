import json

from nltk.tokenize import word_tokenize


def char_freq(text: str) -> dict:
    freq = dict()
    for c in text:
        if c not in freq:
            freq[c] = 0
        freq[c] += 1
    return freq


def word_freq(words: list[str]) -> dict:
    freq = dict()
    for w in words:
        if w not in freq:
            freq[w] = 0
        freq[w] += 1
    return freq


def main():
    filename = "data/tmp/kjv_flat.txt"
    with open(filename, 'r') as fp:
        text = fp.read()

    cf = char_freq(text)
    with open("data/tmp/kjv_flat_chars.json", 'w') as fp:
        cf_ord = sorted(cf.items(), key=lambda x: x[1], reverse=True)
        cf_ord = dict(cf_ord)
        fp.write(json.dumps(cf_ord, indent=4))

    tokens = word_tokenize(text)
    wf = word_freq(tokens)
    with open("data/tmp/kjv_flat_words.json", 'w') as fp:
        wf_ord = sorted(wf.items(), key=lambda x: x[1], reverse=True)
        wf_ord = dict(wf_ord)
        fp.write(json.dumps(wf_ord, indent=4))


if __name__ == "__main__":
    main()
