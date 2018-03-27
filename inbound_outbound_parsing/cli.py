import click
from .parse_csv import parse_one_csv_file
from .parse_text import parse_one_text_file
from sys import stderr


@click.command()
@click.argument('text_files', nargs=-1)
def main(text_files):
    for text_file in text_files:
        try:
            if '.csv' in text_file:
                parser = parse_one_csv_file(text_file)
            else:
                parser = parse_one_text_file(text_file)
            for rec in parser:
                print(rec)

        except AssertionError as ae:
            print('could not parse {} {}'.format(text_file, ae), file=stderr)


if __name__ == '__main__':
    main()
