#!/usr/bin/python3

from bs4 import BeautifulSoup
import click

@click.command()
@click.option('--input_file', required=True, help='glossika memory page source html')
@click.option('--output_file', required=True, help='where to store the csv')
@click.option('--class_id', default="Zg05c", help='The name of the div for the vocab entry')
def do_the_csv_thing(input_file, output_file, class_id):
    with open(input_file) as input_file:
        soup = BeautifulSoup(input_file, 'html.parser')

    lines = []
    all_the_classes = soup.find_all("div", class_=class_id)

    with open(output_file, 'w') as output_csv:
      output_csv.write("meaning,hanzi,pinyin\n")
      for class_ in all_the_classes:
        output_csv.write(( ','.join([child.string for child in class_.children])))
        output_csv.write("\n")

if __name__ == '__main__':
    do_the_csv_thing()
