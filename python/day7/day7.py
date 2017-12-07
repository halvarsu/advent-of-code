import sys
from os import path
import os
sys.path.append( path.dirname( path.dirname( path.abspath(__file__)  )  )  )
from AdventOfCode import AdventOfCode, partition, representsint, sign
import re

class Day7(AdventOfCode):

    """Solves day 7 from adventOfCode.com. """

    def __init__(self, filename='input', test = False):
        """

        :filename: name of the input-file
        :test: overwrites filename and loads file 'test' instead

        """
        if test:
            self._filename = 'test'
        else:
            self._filename = filename
        AdventOfCode.__init__(self, filename = self._filename, day=7)
        self.registries = {}

    def input_prosessor(self, infile):
        return infile.readlines()


    def solve(self, part):
        data = self.get_input()
        programs = []
        for i, line in enumerate(data):
            code1, weight, *references = line.split()
            weight = int(weight.strip('()'))
            prog1 = Program(code1, weight, definition = line)
            try:
                prog1 = programs[programs.index(prog1)]
                prog1.set_weight(weight)
                prog1.set_definition(line)
            except ValueError:
                programs.append(prog1)
            if references:
                for refcode in references[1:]:
                    code2 = refcode.strip(',')
                    prog2 = Program(code = code2)
                    try:
                        prog2 = programs[programs.index(prog2)]
                    except ValueError:
                        programs.append(prog2)
                    prog1.add_reference(prog2)

        current = programs[-1]
        parents = current.parents()
        while parents:
            if len(parents) > 1:
                print("ERROR, more than one parent")
                break
            else:
                current = parents[0]
                parents = current.parents()
        bottom = current
        print("Bottom node is ", bottom)
        try:
            self.total_weight(bottom)
        except ValueError as err:
            print(str(err))


    def total_weight(self, program):
        disc = program.children()
        total_weight = 0
        weights = []
        for child in disc:
            child_weight = child.get_weight() + self.total_weight(child)
            weights.append(child_weight)
        if len(set(weights)) > 1:
            print([str(c) for c in program.children()])
            msg = "Unbalanced disc at node " + str(program) + ", "+ str(weights) + ". "
            raise ValueError(msg)
        return sum(weights)




        


class Program(object):

    """Docstring for Program. """

    def __init__(self, code, weight=0, definition = ''):
        """TODO: to be defined1.

        :code: TODO
        :refers_to: TODO

        """
        self._code = code
        self._weight = weight
        self._refers_to = []
        self._refered_to_by = []
        self._definition = definition if definition else code

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self._code == other._code
        return False

    def __str__(self):
        return str(self._definition)

    def get_code(self):
        return self._code

    def set_weight(self, weight):
        self._weight = weight

    def get_weight(self):
        return self._weight 

    def set_definition(self, definition):
        self._definition = definition

    def add_reference(self, other):
        self._refers_to.append(other)
        other._refered_to_by.append(self)

    def parents(self):
        return self._refered_to_by

    def children(self):
        return self._refers_to

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--test',help='run testfile',
            action ='store_true',default=False)
    parser.add_argument('-p','--part',help='select part',
            choices =[1,2],default=1, type=int)
    args = parser.parse_args()

    day7 = Day7(test = args.test)
    print(day7.solve(part = args.part))
    #p1 = Program(code = 123)
    #p2 = Program(code = 123)
    #print(p1 == p1)
    #a = [p1]
    #print(p1 in a)
    #p3 = Program(code = 555)
    #print(a.index(p3))

