
def parse_data_table(tablefile):
    with open(tablefile) as tf:
        for line in tf:
            tkns = line.strip().split()
            try:
                yield tkns[0], tkns[4], tkns[1], tkns[2]
            except KeyError:
                pass


def parse_namefiles(namefiles):
    tripToSL, slToTrip = {}, {}
    for namefile in namefiles:
        for slName, tripName in parse_one_namefile(namefile):
            tripToSL[tripName] = slName
            slToTrip[slName] = tripName
    return tripToSL, slToTrip


def parse_one_namefile(namefile):
    with open(namefile) as nf:
        for line in nf:
            tkns = line.strip().split()
            try:
                yield tkns[2], tkns[3]
            except KeyError:
                pass


def get_msub_project(filepath):
    tkns = filepath.split('/')
    return tkns[0]


def get_seq_project(filepath):
    tkns = filepath.split('/')
    if len(tkns) >= 3:
        return tkns[1]
    return ''


def get_flowcell(filepath):
    tkns = filepath.split('/')
    if len(tkns) >= 4:
        return tkns[2]
    return ''


def get_sl_name(filename, tripToSL):
    endings = ['_1.fastq.gz', '_2.fastq.gz']
    base = None
    for ending in endings:
        if ending in filename:
            base = filename.split(ending)[0]
    if base is None:
        return ''
    if 'SL' in base:
        return base
    else:
        return tripToSL[base]


def get_trip_name(filename, slToTrip):
    endings = ['_1.fastq.gz', '_2.fastq.gz']
    base = None
    for ending in endings:
        if ending in filename:
            base = filename.split(ending)[0]
    if base is None:
        return ''
    if 'SL' in base:
        return slToTrip[base]
    else:
        return base
