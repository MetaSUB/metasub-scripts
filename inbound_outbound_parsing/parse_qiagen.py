import click
import pandas as pd


'''
qiagen data comes in these super cute excel files.

Just look at one
'''


def extract_grid(grid):
    out = {}
    for r in range(1, 9):
        rname = 'ABCDEFGH'[r - 1]
        for c in range(1, 13):
            cname = str(c)
            if len(cname) == 1:
                cname = '0' + cname
            key = rname + cname
            val = grid.iloc[r + 1, c]
            out[key] = val
    return out


def get_grids(tbl):
    nrows = tbl.shape[0]
    ngrids = (nrows + 1) // 11
    out = {}
    for n in range(ngrids):
        ind = 11 * n
        positions = tbl.iloc[ind:(ind + 10), 0:13]
        positions = extract_grid(positions)
        conc = tbl.iloc[ind:(ind + 10), 14:27]
        conc = extract_grid(conc)
        out[n + 1] = (positions, conc)
    return out


def grid_to_recs(num, grid, prefix=None):
    platename = 'plate_{}'.format(num)
    if prefix is not None:
        platename = '{}_{}'.format(prefix, platename)
    names, concs = grid
    recs = []
    for pos, name in names.items():
        conc = concs[pos]
        rec = '{} {} {} {}'.format(platename, pos, name, conc)
        recs.append(rec)
    return recs


@click.command()
@click.option('-p', '--prefix', default=None)
@click.argument('excel_file')
def main(prefix, excel_file):
    tbl = pd.read_excel(excel_file, header=None)
    grids = get_grids(tbl)
    for n, grid in grids.items():
        for rec in grid_to_recs(n, grid, prefix=prefix):
            print(rec)


if __name__ == '__main__':
    main()
