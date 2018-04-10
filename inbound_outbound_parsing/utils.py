from os.path import dirname


city_name_table = None

def parse_name_table_file():
    table_file_name = dirname(__file__) + '/../city_names.csv'
    with open(table_file_name) as tf:
        tf.readline()
        city_name_table = {}
        for line in tf:
            tkns = line.strip().split(',')
            if len(tkns) == 2:
                city_name, country_name = tkns[0].lower(), tkns[1].lower()
                try:
                    city_name_table[city_name].add(country_name)
                except KeyError:
                    city_name_table[city_name] = set()
                    city_name_table[city_name].add(country_name)

    return city_name_table


def parse_name_table():
    global city_name_table
    if city_name_table is not None:  # this is a dirty hack, forgive me
        return city_name_table
    city_name_table = parse_name_table_file()
    #global city_name_table
    return city_name_table


def validate_city_names(rackname):
    city_tbl = parse_name_table()
    tkns = [tkn.lower() for tkn in rackname.split('_')]

    city_name = None
    for tkn in tkns:
        if tkn in city_tbl:
            city_name = tkn
    if city_name is None:
        raise AssertionError('No valid city name in {}'.format(rackname))

    if len(tkns) == 1:
        return rackname

    country_name = None
    for tkn in tkns:
        if tkn in city_tbl[city_name]:
            country_name = tkn
    if country_name is None:
        msg = 'No valid country name in {} matching city {}'
        msg = msg.format(rackname, city_name)
        raise AssertionError(msg)

    return rackname


def clean_plate_position(pos):
    pos = pos.strip()
    while pos[-1] not in [str(el) for el in range(10)]:
        pos = pos[:-1]
    assert pos[0] in 'ABCDEFGH'
    assert len(pos) in [2, 3]
    if len(pos) == 2:
        pos = pos[0] + '0' + pos[1]
    return pos


def clean_rackname(rawrackname, check_city_names=True):
    rackname = rawrackname.strip().lower()
    rackname = switch(rackname, '.', '')
    rackname = switch(rackname, '(', '')
    rackname = switch(rackname, ')', '')
    rackname = switch(rackname, ',', '')
    rackname = switch(rackname, '-', '_')
    rackname = switch(rackname, ' ', '_')
    for c in rackname:
        if c not in 'abcdefghijklmnopqrstuvwxyz0123456789_':
            msg = '{} ({}) is not an approved character for a rackname'
            msg = msg.format(c, rawrackname)
            raise AssertionError(msg)

    if check_city_names:
        validate_city_names(rackname)

    return rackname


def clean_bc(rawbc):
    bc = rawbc.strip().lower()
    if bc == 'no read':
        return 'no_read'
    elif bc == 'no tube':
        return 'no_tube'
    for c in bc:
        if c not in '0123456789':
            msg = '{} ({}) is not an approved character for a bc'
            msg = msg.format(c, rawbc)
            raise AssertionError(msg)
    return bc


def switch(s, a, b):
    return b.join(s.split(a))
