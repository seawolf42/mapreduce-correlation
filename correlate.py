import math
import mincemeat
import sys


def read_data(filename='data1.csv'):
    with open(filename) as infile:
        lines = infile.read().split('\n')
        headers = lines[0].split(',')
        lines = [ line.split(',') for line in lines[1:-1] ]
    data = { line[0]: [ float(x) for x in line[1:] ] for line in lines }
    return headers, data


def mapfn(key, value):
    for i in range(len(value)):
        for j in range(i+1, len(value)):
            yield (i,j), (value[i], value[j])


def reducefn(key, values):
    x = 0.
    y = 0.
    xx = 0.
    yy = 0.
    xy = 0.
    n = 0
    for (xk,yk) in values:
        x += xk
        y += yk
        xx += xk ** 2
        yy += yk ** 2
        xy += xk * yk
        n += 1
    numerator = xy - (x*y)/n
    denominator1 = xx - (x**2)/n
    denominator2 = yy - (y**2)/n
    import math
    denominator = math.sqrt(denominator1 * denominator2)
    return numerator/denominator


def run_server(filename):
    s = mincemeat.Server()
    headers, data = read_data(filename)
    s.datasource = data
    s.mapfn = mapfn
    s.reducefn = reducefn
    results = s.run_server(password="changeme")
    for r in sorted(results):
        print (headers[r[0]+1], headers[r[1]+1]), results[r]

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else 'data1.csv'
    run_server(filename)
