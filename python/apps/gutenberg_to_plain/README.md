# gutenberg_to_plain
## Sample run
Requires: Python 3.x (tested with x=12+)

The description below assumes you are in the root folder.

```bash
export PYTHONPATH=python
python python/apps/gutenberg_to_plain/main.py data/pgBible.txt data/tmp/kjv_plaintext
```
If everything worked you will have a lot of new folders and files below the folder ```data/tmp/kjv_plaintext```.

### Data output
The file contents generated are stripped of book names, chapter and verse notations.

The text in each generated file consists of the verses flattened out. One verse per row for the entirety of the specified book (see lists below).

### Folders at ```data/tmp/kjv_plaintext```:
* 01/ - Chapter files for the first book in the Bible, Genesis.
* 02/ - Chapter files for the second book in the Bible, Exodus.
* ...
* 66/ - Chapter files for the 66'th book in the Bible, Revelation
Below each folder there exists one file per chapter of the book.

### Files at ```data/tmp/kjv_plaintext```:
* 01.txt - Verses for the entire first book in the Bible, Genesis.
* 01.txt - Verses for the entire first book in the Bible, Genesis.
* ...
* 66.txt - Verses for the entire first book in the Bible, Genesis.
* bible.txt - Verses for the entire Bible.

## Development
To run tests, and to develop, it is recommended to add pytest.
There is an environment file, designed for conda:
 * environment.yml

To install the environment you need to install Anaconda, then open a conda console and run:
```bash
conda env create -f python/environment.yml
```
After this an enviroment called ```scriptus_1``` is available.
Run this to switch to the environment:
```bash
conda activate scriptus_1
```
