import sys
from os import path
import os
sys.path.append( path.dirname( path.dirname( path.abspath(__file__)  )  )  )
from AdventOfCode import AdventOfCode, partition, representsint, sign
import re

class Day15(AdventOfCode):

    """Solves day 15 from adventOfCode.com. """

    def __init__(self, filename='input', test =False):
        """

        :filename: name of the input-file
        :test: overwrites filename and loads file 'test' instead

        """
        if test:
            self._filename = 'test'
        else:
            self._filename = filename
        AdventOfCode.__init__(self, filename = self._filename, day=15)
        self.registries = {}

    def input_prosessor(self, infile):
        counts = []; starts = []
        for line in infile:
            l = re.findall(r'[\d]+', line)
            counts.append(int(l[1]))
            starts.append(int(l[3]))
        return counts, starts

    
    def solve(self, part):
        self.counts, self.pos = self.get_input()
        if part == 2:
            self.counts.append(11)
            self.pos.append(0)
        for i in range(len(self.pos)):
            self.pos[i] = (self.pos[i]+i+1)%self.counts[i]
        j = 0
        while not self.all_zeros():
            for i in range(len(self.pos)):
                self.pos[i] = (self.pos[i]+1)%self.counts[i]
            j+=1
        return j

    def all_zeros(self):
        return all(p==0 for p in self.pos)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--test',help='run testfile',
            action ='store_true',default=False)
    parser.add_argument('-p','--part',help='select part',
            choices =[1,2],default=1, type=int)
    args = parser.parse_args()

    day15 = Day15(test = args.test)
    print day15.solve(part = args.part)

