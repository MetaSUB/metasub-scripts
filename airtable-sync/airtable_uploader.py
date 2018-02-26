import airtable
from time import sleep
from os.path import basename, isfile
from .util_parsers import *


BASE_ID = 'appnanDiqnz1N0cUy'
TABLE_ID = 'Table 1'


def create_uploader(api_key):
    at = airtable.Airtable(BASE_ID, api_key)

    def uploader(data):
        sleep(0.2)
        return at.create(TABLE_ID, data)
    return uploader


def create_data(filepath,
                md5, linecount, filesize,
                slToTrip, tripToSL):
    seqcount = int(linecount) / 4
    filename = basename(filepath)
    data = {
        'File Name': filename,
        'File Path': filepath,
        'md5sum': md5,
        'Num Seqs': seqcount,
        'File Size': int(filesize),
        'MetaSUB Project': get_msub_project(filepath),
        'Sequencing Project': get_seq_project(filepath),
        'Flowcell': get_flowcell(filepath),
        'SL Name': get_sl_name(filename, tripToSL),
        'Triplicate Name': get_trip_name(filename, slToTrip)
    }
    return data


@click.command()
@click.argument('api_key')
@click.argument('tblfile')
@click.argument('namefiles')
def main(api_key, tblfile, namefiles):
    tripToSL, slToTrip = parse_namefiles(namefiles)
    uploader = create_uploader(api_key)
    for filepath, md5, linecount, filesize in parse_data_table(tblfile):
        if not isfile(filepath):
            continue
        data = create_data(filepath,
                           md5, linecount, filesize,
                           slToTrip, tripToSL)
        reply = uploader(data)
        print(reply)


if __name__ == '__main__':
    main()

