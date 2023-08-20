# Glossika Vocab Scraper

## Description

Given the source html of a Glossika memory page, pull out a CSV of your sentances with the translation, the hanzi, and the pinyin.

## Usage
### Obtain your memory html

1. Log into you glossika account on desktop
2. Go to https://ai.glossika.com/app/progress/memory
3. Inspect the page
4. In the inspector, copy the HTML block with all childen
5. Paste the HTML into a file and save it

NB: 'View Source' will not contain your vocabulary words. You have to go through the inspector panel because the modern web is _great_

### Run the script
```bash
./glossika-scraper.py --input_file data/glossika-memory-2.html --output_file output/test2.csv
```

```bash
Usage: glossika-scraper.py [OPTIONS]

Options:
  --input_file TEXT   glossika memory page source html  [required]
  --output_file TEXT  where to store the csv  [required]
  --class_id TEXT     The name of the div for the vocab entry
  --help              Show this message and exit.
```

## Disclaimer

I wrote this in about 30 minutes as an exercise in working in python again.
Also to get my vocabulary words from glossika though. So it does work, at least for now!

## Next Steps

- [ ] Make the script take an input directory and process all files into one csv
- [ ] ??? Oauth and scrap the actual memory pages ??? Might be breaking Glossika TOS? Doublecheck first.
