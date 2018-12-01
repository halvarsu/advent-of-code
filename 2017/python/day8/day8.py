import sys
from os import path
import os
sys.path.append( path.dirname( path.dirname( path.abspath(__file__)  )  )  )
from AdventOfCode import AdventOfCode, partition, representsint, sign
import re

class Day8(AdventOfCode):

    """Solves day 8 from adventOfCode.com. """

    def __init__(self, filename='input', test = False):
        """

        :filename: name of the input-file
        :test: overwrites filename and loads file 'test' instead

        """
        if test:
            self._filename = 'test'
        else:
            self._filename = filename
        AdventOfCode.__init__(self, filename = self._filename, day=8)
        self.registries = {}

    def inc(self, reg_val, num):
        return  reg_val + num

    def dec(self, reg_val, num):
        return  reg_val - num

    def le(self, reg_val, num):
        return  reg_val <= num

    def lt(self, reg_val, num):
        return  reg_val < num

    def ge(self, reg_val, num):
        return  reg_val >= num

    def gt(self, reg_val, num):
        return  reg_val > num

    def ne(self, reg_val, num):
        return  reg_val != num

    def eq(self, reg_val, num):
        return  reg_val == num


    def input_prosessor(self, infile):
        return [self.line_prosessor(line) for line in infile]

    def line_prosessor(self, line):
        keys = ["reg", "op", "amount", "if", "test_reg", "test", "test_val"]
        values = line.split()
        return values #{k:v for k,v in zip(keys,values)}

    def solve(self, part):
        operators = {"inc":self.inc, "dec":self.dec}
        test_func = {"<=":self.le, "<":self.lt, ">=":self.ge, ">":self.gt,
                "!=":self.ne, "==":self.eq}
        data = self.get_input()
        data = self.get_input()
        registers = {}
        print(len(data))
        max_val = 0
        for instr in data:
            reg = instr[0]
            op = operators[ instr[1] ]
            amount = int(instr[2])
            _ = instr[3]
            test_reg = instr[4]
            test = test_func[instr[5]]
            test_amount = int(instr[6])

            reg_val = registers.get(reg, 0)
            test_val = registers.get(test_reg, 0)

            registers[reg] = op(reg_val, amount) if test(test_val, test_amount) else reg_val
            max_val = max([registers[reg], max_val])

        keys = registers.keys()
        
        print(max(registers.values()))
        print(max_val)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--test',help='run testfile',
            action ='store_true',default=False)
    parser.add_argument('-p','--part',help='select part',
            choices =[1,2],default=1, type=int)
    args = parser.parse_args()

    day8 = Day8(test = args.test)
    print(day8.solve(part = args.part))

