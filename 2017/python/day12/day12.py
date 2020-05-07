import sys
from os import path
import os
sys.path.append( path.dirname( path.dirname( path.abspath(__file__)  )  )  )
from AdventOfCode import AdventOfCode, partition, representsint, sign
import re

class Day12(AdventOfCode):

    """Solves day 12 from adventOfCode.com. """

    def __init__(self, filename='input', test =False):
        """

        :filename: name of the input-file
        :test: overwrites filename and loads file 'test' instead

        """
        if test:
            self._filename = 'test'
        else:
            self._filename = filename
        AdventOfCode.__init__(self, filename = self._filename, day=12)
        self.registries = {}

    def input_prosessor(self, infile):
        return map(self.line_prosessor, infile)

    def line_prosessor(self, line):
        return line.split()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--test',help='run testfile',
            action ='store_true',default=False)
    parser.add_argument('-p','--part',help='select part',
            choices =[1,2],default=1, type=int)
    args = parser.parse_args()

    day12 = Day12(test = args.test)
    print day12.solve(part = args.part)

