# Glossika Vocab Scraper
## Description
Given the source html of a user's Glossika memory page, pull out a CSV of the sentances components.

Tested on the Chinese (Taiwan) course; returns a csv of the English sentence, the Chinese hanzi, and the pinyin.

This is meant to work with an existing subscription to the new online glossika courses, either to create supplemental study materials or to do an export of your memory as you are finishing with Glossika. It only pulls the sentences in your personal memory bank. If you learn more sentences, you will need to rerun this process.

This code has no connection to the older glossika pdf & audio offline coursework.

## Usage
### Setup this repo
1. Clone this repo
2. Install [pipenv](https://pypi.org/project/pipenv/)
3. Run `pipenv install`

(Or use your preferred python dependency manager)

### Obtain your memory htmls
1. Log into you glossika account on desktop
2. Go to https://ai.glossika.com/app/progress/memory
3. Inspect the page
4. In the inspector, copy the HTML block with all childen
5. Paste the HTML into a file and save it into the data directory as `glossika-N.html`, where N is the page number
6. Repeat for each pagination.

**NB:** 'View Source' will not contain your vocabulary words. You have to go through the inspector panel because the modern web is _great_.

**NB:** You should doublecheck the class name for the div around each vocabulary entry. Pass it in via the class_id argument if its anything other than 'Zg05c'

### Run the script
```bash
./glossika-scraper.py --input_dir data --output_file output/glossika_vocab.csv
```

```bash
Usage: glossika-scraper.py [OPTIONS]

Options:
  --input_dir TEXT    relative path to the direcotory comtaining glossika
                      memory page source html. Expects files to start with
                      glossika and be .html  [required]
  --output_file TEXT  the csv output file  [required]
  --class_id TEXT     The name of the div for the vocab entry
  --help              Show this message and exit.
Usage: glossika-scraper.py [OPTIONS]
```

## Disclaimer
I wrote this half to have my vocabulary and half to just muck around in python again.
It does work! But its not the most robust.

