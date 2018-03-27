from airtable import airtable
import click
from .utils import *
from time import sleep


BASE_ID = 'appnanDiqnz1N0cUy'


def create_data(line):
    tkns = line.strip().split()
    rack = tkns[0]
    pos = tkns[1]
    bc = tkns[2]
    uuid = '{}__{}'.format(rack, pos)
    data = {
        'name': uuid,
        'rack': rack,
        'position': pos,
        'barcode': bc
    }
    return data


def create_uploader(table_name, api_key):
    at = airtable.Airtable(BASE_ID, api_key)
    def uploader(data):
        sleep(0.2)
        return at.create(table_name, data)
    return uploader


@click.command()
@click.argument('table_name')
@click.argument('api_key')
@click.argument('plate_file')
def main(table_name, api_key, plate_file):
    uploader = create_uploader(table_name, api_key)
    with open(plate_file) as pf:
        for line in pf:
            data = create_data(line)
            reply = uploader(data)
            print(reply)


if __name__ == '__main__':
    main()