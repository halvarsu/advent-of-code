import sys
from os import path
import os
sys.path.append( path.dirname( path.dirname( path.abspath(__file__)  )  )  )
from AdventOfCode import AdventOfCode, partition, representsint, sign
import re

class Day16(AdventOfCode):

    """Solves day 16 from adventOfCode.com. """

    def __init__(self, filename='input', test =False):
        """

        :filename: name of the input-file
        :test: overwrites filename and loads file 'test' instead

        """
        self._test = test
        self._filename = filename
        AdventOfCode.__init__(self, filename = self._filename, day=16)
        self.registries = {}

    def input_prosessor(self, infile):
        return infile.readline().split()[0]

    def solve(self, part):
        tot = self.get_input()
        while len(tot) < 272:
            tot = tot + '0' + ''.join('0' if b == '1' else '1' for b in tot[::-1])
        tot = tot[:272]

        chcksm = tot
        new = ''
        if self._test:
            chcksm = '110010110100'
        l = len(chcksm)
        while not l%2:
            print chcksm, l
            for i in range(0,l,2):
                #print i
                if chcksm[i] == chcksm[i+1]:
                    new += '1'
                else:
                    new += '0'
            chcksm = new
            new = ''
            l = len(chcksm)
        self.sol = chcksm
        return chcksm

    def save(self,  part):
        sol = self.sol
        with open('part%d.txt'%part, 'w') as outfile:
            outfile.write(sol)

        



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--test',help='run testfile',
            action ='store_true',default=False)
    parser.add_argument('-p','--part',help='select part',
            choices =[1,2],default=1, type=int)
    args = parser.parse_args()

    day16 = Day16(test = args.test)
    print day16.solve(part = args.part)
    day16.save(part = args.part)

