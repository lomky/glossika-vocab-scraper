#!/usr/bin/python3
"""Given an input dir, take all the glossika htmls and turn them into a csv"""

from pathlib import Path
from bs4 import BeautifulSoup
import click

# pylint: disable=no-value-for-parameter
@click.command()
@click.option('--input_dir',
        required=True,
        help='relative path to the direcotory comtaining glossika memory page source html.\
                Expects files to start with glossika and be .html')
@click.option('--output_file', required=True, help='the csv output file')
@click.option('--class_id', default="Zg05c", help='The name of the div for the vocab entry')
def do_the_csv_thing(input_dir, output_file, class_id):
    """Given an input dir, take all the glossika htmls and turn them into a csv"""
    with open(output_file, 'x', encoding='utf-8') as output_csv:
        output_csv.write("meaning,hanzi,pinyin\n")
    for child in Path(input_dir).glob('glossika*.html'):
        with open(child, encoding='utf-8') as input_file:
            soup = BeautifulSoup(input_file, 'html.parser')

            all_the_classes = soup.find_all("div", class_=class_id)

            with open(output_file, 'a', encoding='utf-8') as output_csv:
                for class_ in all_the_classes:
                    output_csv.write((','.join([child.string for child in class_.children])))
                    output_csv.write("\n")

if __name__ == '__main__':
    do_the_csv_thing()
