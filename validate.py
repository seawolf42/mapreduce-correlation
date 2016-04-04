import csv
import pandas as pd
import sys


def read_data(filename='data1.csv'):
    return pd.io.parsers.read_csv(filename, sep=',', index_col=0)


def validate(data, outfilename):
    correlations = data.corr(method='pearson')
    cols = list(data.columns.values)
    with open(outfilename, 'w') as outfile:
        for i in range(len(cols)):
            for j in range(i+1, len(cols)):
                iname = cols[i]
                jname = cols[j]
                outfile.write('({0},{1})\t{2:.5f}\n'.format(iname, jname, correlations[iname][jname]))


def main():
    infilename = sys.argv[1] if len(sys.argv) > 1 else 'data1.csv'
    outfilename = sys.argv[2] if len(sys.argv) > 2 else 'data1.expected.out'
    data = read_data(infilename)
    validate(data, outfilename)

if __name__ == '__main__':
    main()
