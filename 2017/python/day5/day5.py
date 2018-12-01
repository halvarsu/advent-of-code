import sys
from os import path
import os
sys.path.append( path.dirname( path.dirname( path.abspath(__file__)  )  )  )
from AdventOfCode import AdventOfCode, partition, representsint, sign
import re

class Day5(AdventOfCode):

    """Solves day 5 from adventOfCode.com. """

    def __init__(self, filename='input', test = False):
        """

        :filename: name of the input-file
        :test: overwrites filename and loads file 'test' instead

        """
        if test:
            self._filename = 'test'
        else:
            self._filename = filename
        AdventOfCode.__init__(self, filename = self._filename, day=5)
        self.registries = {}

    def input_prosessor(self, infile):
        return [int(dat) for dat in infile.readlines()]
    
    def solve(self, part):
        if part == 0:
            self.solve(part=1)
            part = 2
        elif part not in [0,1,2]:
            raise ValueError("Invalid part {}".format(part))
        data = self.get_input()
        steps = 0
        pos = 0
        N = len(data)
        while True:
            if pos >= N or pos < 0:
                break
            offset = data[pos]
            if part == 1 or offset < 3:
                data[pos] += 1
            else:
                data[pos] -= 1 
            pos += offset 
            steps   += 1
        print("Part {}: steps taken: {}".format(part,steps))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--test',help='run testfile',
            action ='store_true',default=False)
    parser.add_argument('-p','--part',help='select part',
            choices =[0,1,2],default=0, type=int)
    args = parser.parse_args()

    day5 = Day5(test = args.test)
    print(day5.solve(part = args.part))

