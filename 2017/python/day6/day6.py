import sys
from os import path
import os
sys.path.append( path.dirname( path.dirname( path.abspath(__file__)  )  )  )
from AdventOfCode import AdventOfCode, partition, representsint, sign
import re

class Day6(AdventOfCode):

    """Solves day 6 from adventOfCode.com. """

    def __init__(self, filename='input', test = False):
        """

        :filename: name of the input-file
        :test: overwrites filename and loads file 'test' instead

        """
        if test:
            self._filename = 'test'
        else:
            self._filename = filename
        AdventOfCode.__init__(self, filename = self._filename, day=6)
        self.registries = {}

    def input_prosessor(self, infile):
        data = []
        for d in infile.readline().split():
            d = d.strip('\t\n')
            if d:
                data.append(int(d))
        return data

    def solve(self, part):
        data = self.get_input()

        states = []
        steps = 0
        print(data)
        while data not in states:
            steps+=1
            states.append(data.copy())
            max_index = data.index(max(data))
            val = data[max_index] 
            data[max_index] = 0
            for i in range(val):
                data[(i+max_index+1)%len(data)] += 1
            print(data)

        print("Part 1 solution: ", steps)
        print("Part 2 solution: ", steps - states.index(data))





if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--test',help='run testfile',
            action ='store_true',default=False)
    parser.add_argument('-p','--part',help='select part',
            choices =[1,2],default=1, type=int)
    args = parser.parse_args()

    day6 = Day6(test = args.test)
    print(day6.solve(part = args.part))

