import click


def parse_table(tableFName, namecol=0, sep=' '):
    out = {}
    with open(tableFName) as tbl:
        for line in tbl:
            line = line.strip()
            tkns = line.split(sep)
            name = tkns[namecol]
            out[name] = line
    return out


def cbind(tbl1, tbl2, sep=' '):
    keys = set(tbl1.keys())
    keys |= set(tbl2.keys())
    out = []
    for key in keys:
        l1, l2 = tbl1[key], tbl2[key]
        out.append(l1 + sep + l2)
    return out


@click.command()
@click.option('--c1', default=0, type=int, help='name column for table 1')
@click.option('--c2', default=0, type=int, help='name column for table 2')
@click.argument('table1')
@click.argument('table2')
def main(c1, c2, table1, table2):
    tbl1 = parse_table(table1, namecol=c1)
    tbl2 = parse_table(table2, namecol=c2)
    tbl = cbind(tbl1, tbl2)
    for line in tbl:
        print(line)


if __name__ == '__main__':
    main()
