import sys
from os import path
import os
sys.path.append( path.dirname( path.dirname( path.abspath(__file__)  )  )  )
from AdventOfCode import AdventOfCode, partition, representsint, sign
import re
import numpy as np

class Day4(AdventOfCode):

    """Solves day 4 from adventOfCode.com. """

    def __init__(self, filename='input', test = False):
        """

        :filename: name of the input-file
        :test: overwrites filename and loads file 'test' instead

        """
        if test:
            self._filename = 'test'
        else:
            self._filename = filename
        AdventOfCode.__init__(self, filename = self._filename, day=4)
        self.registries = {}

    def input_prosessor(self, infile):
        return list(map(self.line_prosessor, infile))

    def line_prosessor(self, line):
        return line.split()

    def is_anagram(self, word1, word2):
        anagram = True
        word1 = list(word1)
        word2 = list(word2)
        for letter in word1:
            try:
                pos2 = word2.index(letter)
                word2.pop(pos2)
            except ValueError:
                anagram = False
                break
        if word2:
            anagram = False
        return anagram

    def solve(self,part):
        data = self.get_input()
        self.part1(data)
        data = self.get_input()
        self.part2(data)

    def part1(self,data):
        valid_count = 0
        for line in data:
            valid = True
            while line:
                item = line.pop()
                if item in line:
                    valid = False
            valid_count += valid
        print(valid_count)

    def part2(self,data):
        valid_count = 0
        for line in data:
            valid = True
            while line:
                item = line.pop()
                for other in line:
                    if (item == other) or (self.is_anagram(item,other)):
                        valid = False
            valid_count += valid
        print(valid_count)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--test',help='run testfile',
            action ='store_true',default=False)
    parser.add_argument('-p','--part',help='select part',
            choices =[1,2],default=1, type=int)
    args = parser.parse_args()

    day4 = Day4(test = args.test)
    print( day4.solve(part = args.part))

