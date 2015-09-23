#!/usr/bin/env python
import argparse
import os
import sys

from nxgr.file_finder import FileFinder
from nxgr.file_reader import FileReader


def process_args():
    parser = argparse.ArgumentParser('nxgr')
    parser.add_argument('files', metavar='file', nargs='*',
                        help='Files to be searched', default='.')
    parser.add_argument('-e', dest='re', required=True)
    parser.add_argument('--ne', dest='nre')
    parser.add_argument('--frgx', dest='frgx')
    parser.add_argument('--fx', dest='fx')
    parser.add_argument('--fnrgx', dest='fnrgx')

    args = parser.parse_args()
    return args


def print_results(data):
    print "{file} +{line}   |{text} ".format(**data)


def file_process_visit(reader):
    def visit_file(f):
        fo = open(f, 'r')
        data = reader.process_file(fo)
        return data
    return visit_file

if __name__ == '__main__':
    main()


def main():
    args = vars(process_args())
    fr = FileReader(pattern=args['re'],
                    negpat=args['nre'],
                    item_visit=print_results)
    frgx = args.get('frgx')

    if args.get('fx'):
        frgx = r'\.%s$' % (args.get('fx'),)

    ff = FileFinder(file_re=frgx, file_nre=args['fnrgx'],
                    visit=file_process_visit(fr))
    ff.read_directory(args['files'])
