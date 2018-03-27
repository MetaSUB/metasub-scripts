from .utils import *


'''
From file: Brisbane_Australia_1_20171101_103038.csv

20171101,10:29:29,01,A,0235059188
20171101,10:29:29,02,A,0235037784
20171101,10:29:29,03,A,0235059174
20171101,10:29:29,04,A,0235059173
20171101,10:29:29,05,A,0235062851
'''


def parse_one_csv_file(fname):
    rackname = clean_rackname(fname.split('/')[-1].split('.csv')[0])
    recs = []
    with open(fname) as f:
        for line in f:
            try:
                line = line.strip()
                if len(line) == 0:
                    continue
                tkns = line.split(',')
                row = tkns[3]
                col = tkns[2]
                pos = clean_plate_position(row + col)
                bc = clean_bc(tkns[4])
                out = '{} {} {}'.format(rackname, pos, bc)
                recs.append(out)
            except Exception:
                print('failed to parse line: "{}"'.format(line))
                raise
    return recs
