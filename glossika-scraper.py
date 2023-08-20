#!/usr/bin/python3

from bs4 import BeautifulSoup
from pathlib import Path
import click
import os

@click.command()
@click.option('--input_dir', required=True, help='relative path to the direcotory comtaining glossika memory page source html. Expects files to start with glossika and be .html')
@click.option('--output_file', required=True, help='the csv output file')
@click.option('--class_id', default="Zg05c", help='The name of the div for the vocab entry')
def do_the_csv_thing(input_dir, output_file, class_id):
    with open(output_file, 'x') as output_csv:
        output_csv.write("meaning,hanzi,pinyin\n")
    for child in Path(input_dir).glob('glossika*.html'):
        with open(child) as input_file:
            soup = BeautifulSoup(input_file, 'html.parser')

            lines = []
            all_the_classes = soup.find_all("div", class_=class_id)

            with open(output_file, 'a') as output_csv:
                for class_ in all_the_classes:
                    save_it = (','.join([child.string for child in class_.children]))
                    output_csv.write(save_it)
                    output_csv.write("\n")

if __name__ == '__main__':
    do_the_csv_thing()
