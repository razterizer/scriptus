# plain_to_flat
## Description
Takes a plain text file (i.e. one row = one verse) and strips it from comma, punctuation etc.
Saves the results to a "flat" file. This means all text is on one single row, without any kind of punctuation etc.

NOTE: For now this is an experimental app for english, meaning "John's" will be simplified to "John".

## Sample run
Required environment specified in ```python/apps/plaintoflat/environment.yml```.
The description below assumes you are in the root folder.

```bash
export PYTHONPATH=python
python python/apps/plain_to_flat/main.py data/tmp/kjv_plaintext/bible.txt data/tmp/kjv_flat.txt
```
