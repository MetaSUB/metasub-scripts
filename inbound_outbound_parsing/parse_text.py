
from .utils import *

'''
$ head Inbound-2\ 26062017\ 035122PM.txt
Date & time of Trace = 26 06 2017 03:51:22 PM
Rack Base Name: Inbound-2
  A01;  0232021993
  A02;  0235196553
  A03;  0235033751

---

inbound_2 A01 0232021993
'''


def parse_one_text_file(fname):
    recs = []
    with open(fname) as f:
        f.readline()  # datetime
        rackname = f.readline().strip()
        rackname = clean_rackname(rackname.split(':')[1])
        for line in f:
            try:
                line = line.strip()
                if len(line) == 0:
                    continue
                tkns = line.split(';')
                pos = clean_plate_position(tkns[0])
                bc = clean_bc(tkns[1])
                out = '{} {} {}'.format(rackname, pos, bc)
                recs.append(out)
            except Exception:
                print('failed to parse line: "{}"'.format(line))
                raise
    return recs
