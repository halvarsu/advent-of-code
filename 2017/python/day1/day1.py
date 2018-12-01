import sys
from os import path
import os
sys.path.append( path.dirname( path.dirname( path.abspath(__file__)  )  )  )
from AdventOfCode import AdventOfCode, partition, representsint, sign
import re

class Day1(AdventOfCode):

    """Solves day 1 from adventOfCode.com. """

    def __init__(self, filename='input', test_file = False):
        """

        :filename: name of the input-file
        :test_file: overwrites filename and loads file 'test_file' instead

        """
        if test_file:
            self._filename = 'test'
        else:
            self._filename = filename
        AdventOfCode.__init__(self, filename = self._filename, day=1)
        self.registries = {}

    def input_prosessor(self, infile):
        return list(map(self.line_prosessor, infile))[0]

    def line_prosessor(self, line):
        return str(line)

    def solve(self, part):
        if part == 1:
            self.part1()
        elif part == 2:
            self.part2()
        else:
            self.part1()
            self.part2()

    def part1(self):
        data = self.get_input()
        s = 0
        for i in range(len(data)):
            if data[i] == data[(i+1)%(len(data)-1)]:
                s+=int(data[i])
        print(s)

    def part2(self):
        data = self.get_input()
        s = 0
        datalen = len(data)
        for i in range(len(data)):
            if data[i] == data[(i+int(datalen/2))%(datalen-1)]:
                s+=int(data[i])
        print(s)
        




if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--test_file',help='run testfile',
            action ='store_true',default=False)
    parser.add_argument('-p','--part',help='select part',
            choices =[1,2],default=1, type=int)
    args = parser.parse_args()

    day1 = Day1(test_file = args.test_file)
    print( day1.solve(part = args.part))

