import sys
from os import path
import os
sys.path.append( path.dirname( path.dirname( path.abspath(__file__)  )  )  )
from AdventOfCode import AdventOfCode, partition, representsint, sign
import re
import md5

class Day14(AdventOfCode):

    """Solves day 14 from adventOfCode.com. """

    def __init__(self, inp ='', test = False, part = 1):
        """

        :filename: name of the input-file
        :test: overwrites filename and loads file 'test' instead

        """
        if inp:
            self._input = inp
        elif test:
            self._input = 'abc'
        else:
            self._input = 'zpqevtbw'
        self._part = part
        self.prev_hash_count = 0
        self.hash_count = 0
        self.keys = []
        self.hashes = []

    def get_input(self):
        return self._input

    def get_3s(self, string):
        return re.findall(r'(\w)\1{2,}', string)

    def got_5(self, char, string):
        if char == 'any':
            return re.findall(r'(\w)\1{4,}', string)
        else:
            return re.search(r'%s{5,}' % char, string)

    def solve(self):
        inp = self.get_input()
        base = md5.new()
        base.update(inp)
        i=0
        while len(self.keys) < 64:
            m = base.copy()
            m.update(str(i))
            s = m.hexdigest()
            self.hash_count += 1
            if self._part == 2:
                s = self.hash_mania(s)
            chars = self.get_3s(s)
            if chars:
                if self._part == 2:
                    print chars, s, i, self.hash_count, len(self.keys)
                char = chars[0] 
                for j in range(1,1001):
                    m2 = base.copy()
                    m2.update(str(i+j))
                    s2 = m2.hexdigest()
                    self.hash_count += 1
                    if self._part == 2:
                        s2 = self.hash_mania(s2)
                    if self.got_5(char, s2):
                        self.keys.append(i)
                        print s
            i += 1
        return self.keys

    def solve2(self):
        """Does the same as solve in perhaps 1/1000 of the time(at 
        least for part 2)"""
        inp = self.get_input()
        self.base = md5.new()
        self.base.update(inp)
        i=0
        while len(self.keys) < 64:
            if len(self.hashes) < (i+1):
                self.add_hash(i)
            h = self.hashes[i]
            chars = self.get_3s(h)
            if chars:
                char = chars[0] 
                for j in range(1,1001):
                    if len(self.hashes) < (i+j+1):
                        self.add_hash(i+j)
                    h2 = self.hashes[i+j]
                    if self.got_5(char, h2):
                        self.keys.append(i)
                        print h, i, j
            i+=1
        return self.keys
                

    def add_hash(self,i):
        m = self.base.copy()
        m.update(str(i))
        s = m.hexdigest()
        if self._part == 2:
            s = self.hash_mania(s)
        self.hashes.append(s)


    def hash_mania(self, s):
        for i in range(2016):
            m = md5.new()
            m.update(s)
            s = m.hexdigest()
        self.hash_count += 2016
        return s



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--test',help='run testfile',
            action ='store_true',default=False)
    parser.add_argument('-p','--part',help='select part',
            choices =[1,2],default=1, type=int)
    parser.add_argument('-s','--solver',help='choose solver',
            choices =[1,2],default=2,type=int)
    args = parser.parse_args()

    day14 = Day14(test = args.test,part = args.part)
    if args.solver == 2:
        print day14.solve2()
    elif args.solver == 1: 
        print day14.solve()
    else:
        print "You shouldn't be here"

