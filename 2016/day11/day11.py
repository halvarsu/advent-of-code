import sys
from os import path
import os
sys.path.append( path.dirname( path.dirname( path.abspath(__file__)  )  )  )
from AdventOfCode import AdventOfCode, partition
import re

class Day11(AdventOfCode):

    """Was supposed to solve day 11 of AdventOfCode.com trough an 
    extreme brute force method, turned into a game instead. """

    def __init__(self, easy_mode =False):
        """

        :filename: name of the input-file

        """
        if easy_mode:
            self._filename = 'test'
        else:
            self._filename = 'input'
        AdventOfCode.__init__(self, filename = self._filename, day=11)
        self.prev_states = []
        self.num_moves = []
        self.element_count = 0

    def line_prosessor(self, line):
        # re wont split on '-' ... Made this a bit uglier
        contents = re.split(r'[ -,]',line.strip('.\n\r'))
        contains = []
        elements = {'promethium':'1','cobalt':'2','curium':'3',
                     'ruthenium':'4','plutonium':'5'}
        object_type = {'microchip':'M', 'generator':'G'}
        try:
            i = contents.index('a')
            while True:
                item = contents[i+1:i+3]
                s = item[0]
                if '-' in s:
                    s = elements[s[:s.find('-')]]
                else:
                    s = elements[s]

                o = item[1]
                if '.' in o:
                    o = object_type[o[:-1]]
                else:
                    o = object_type[o]

                contains.append(s+o)
                i = contents.index('a',i+1)
        except ValueError:
            pass
        return contains

    def __str__(self):
        s = ''
        E = self.elevator
        types = ["%dM" %(i+1) for i in range(self.element_count)]\
                +["%dG" %(i+1) for i in range(self.element_count)] 
        types = sorted(types)

        i = len(self.data)-1
        while i >= 0:
            s+='F%d' %i
            s+=' E ' if E==i else ' . '
            s+=' '.join(
                [elem if elem in data[i] else ' .' for elem in types])
            s+= '\n' if i != 0 else ''
            i-=1
        return s
        
    def input_prosessor(self, infile):
        self.data = map(self.line_prosessor, infile)
        return self.data

    def get_state(self,data):
        state = ""
        for i, line in enumerate(data):
            state += str(i)+"".join(sorted(line))
        return state

    def data_from_state(self,state):
        '''To be made'''
        data = [[] for i in range(4)]
        for i in state:
            pass
        return NotImplementedError

    def check_validity(self,items):
        generators, chips = partition(items,lambda x:(x[1]=='G') )
        if generators:
            for c in chips:
                if '{}G'.format(c[0]) not in generators:
                    return False
        return True

    def done(self,data):
        for line in data[:-1]:
            if line:
                return False
        return True

    def game(self,data=None,E=0, moves=0):
        if not data:
            data = self.data
            print "HEI"
        else:
            self.data = data
        self.element_count = max(map(lambda x: int(x[0]),
            [i for j in data for i in j]))

        self.elevator = E
        while True:
            items = data[E]
            if not self.check_validity(items):
                print "YOU HAVE LOST: GAME OVER."
                break
            os.system('clear')
            if self.done(data):
                self.num_moves.append(moves)
                print 'You win! Done in ', moves,'moves!'
                a = raw_input('play again?')
                return a
            self.data = data
            state = self.get_state(data)

            print "This is the setup:       (moves %d)" %moves
            print self

            if state in self.prev_states:
                print "You might have seen this setup before..."
                self.prev_states.append(state)
            else:
                self.prev_states.append(state)

            data, to = self.move(data,E)
            E = to
            moves += 1
            self.elevator = E


    def move(self, data, E):
        items = data[E]
        targets=[j for j in (E-1,E+1) if j in range(len(data))] 
        to = self.prompt('Where do you want to move?',
                        targets, int, 'F{}')
        count = self.prompt('How any items to move?', 
                            range(1,3),int)
        for k in range(count):
            item = self.prompt( 'Select item %d:'%(k+1),sorted(items))
            data[to].append(data[E].pop(data[E].index(item)))
        return data, to



    def prompt(self, prompt_string, seq, typ=str, pad ='{}'):
        f_seq = map(pad.format,seq)
        choices = f_seq+ seq

        try:
            prompt_string +='\n['+', '.join(map(str,seq))+']\n/'
            result = typ(raw_input(prompt_string))
            print result
            if result in choices:
                return result
            else:
                raise ValueError
        except ValueError:
            os.system('clear')
            print self
            self.prompt("Invalid choice, try again: ",seq,typ,pad)
            
if __name__ == "__main__":
    day11 = Day11()
    data =day11.get_input()
    print day11.game()



