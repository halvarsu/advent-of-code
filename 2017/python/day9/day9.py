import sys
from os import path
import os
sys.path.append( path.dirname( path.dirname( path.abspath(__file__)  )  )  )
from AdventOfCode import AdventOfCode, partition, representsint, sign
import re

class Day9(AdventOfCode):

    """Solves day 9 from adventOfCode.com. """

    def __init__(self, filename='input', test = False):
        """

        :filename: name of the input-file
        :test: overwrites filename and loads file 'test' instead

        """
        if test:
            self._filename = 'test'
        else:
            self._filename = filename
        AdventOfCode.__init__(self, filename = self._filename, day=9)
        self.registries = {}

    def input_prosessor(self, infile):
        line = infile.readline()[:-1] # drop newline
        return line


    def solve(self, part):
        data = self.get_input()
        total = 0
        group_nesting = 0
        is_garbage = False
        is_escaped = False
        removed = 0
        for char in data:
            if is_escaped:
                is_escaped = False
                continue
            if is_garbage:
                if char == '>':
                    is_garbage = False
                elif char == "!":
                    is_escaped = True
                else:
                    removed += 1
                continue
            if char == "{":
                group_nesting += 1
            elif char == "}" and group_nesting > 0:
                total += group_nesting
                group_nesting -= 1
            elif char == "!":
                is_escaped = True
            elif char == "<":
                is_garbage = True

        print(total, removed)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--test',help='run testfile',
            action ='store_true',default=False)
    parser.add_argument('-p','--part',help='select part',
            choices =[1,2],default=1, type=int)
    args = parser.parse_args()

    day9 = Day9(test = args.test)
    print(day9.solve(part = args.part))

