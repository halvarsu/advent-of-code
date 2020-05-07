import sys
from os import path
import numpy as np
import os
sys.path.append( path.dirname( path.dirname( path.abspath(__file__)  )  )  )
from AdventOfCode import AdventOfCode, partition, representsint, sign
import re

class Day3(object):

    """Solves day 3 from adventOfCode.com. """

    def __init__(self, filename='input', test= False):
        """

        :filename: name of the input-file
        :test: overwrites filename and loads file 'test' instead

        """
        if test:
            self._filename = 'test'
        else:
            self._filename = filename
        AdventOfCode.__init__(self, filename = self._filename, day=3)
        self.registries = {}

    def get_input(self):
        return 325489

    def sawtooth(self, i, period, amplitude):
        return amplitude*np.abs(0.5*period - (i%period))

    def radial_distance(self, i):
        return np.ceil(np.sqrt(i)/2+0.5) - 1

    def angular_distance(self, i):
        # does some magic. 
        if i == 1:
            return 0
        level = self.radial_distance(i) 
        core = (2*(level)-1)**2 
        return self.sawtooth(i-core, 2*level, level)/level #, core,level,i

    def solve(self, part):
        data = self.get_input()
        if part == 0:
            self.part1(data)
            self.part2(data)
        elif part == 1:
            self.part1(data)
        elif part == 2:
            self.part2(data)
        return 'done'

    def part1(self,data):
        print("Solution part 1:", 
                self.radial_distance(data) + self.angular_distance(data))
        return


    def get_pos(self,i):
        if i == 1:
            return 0,0
        level = self.radial_distance(i) 
        i0 = (2*(level)-1)**2 
        maxpos = level
        angle = i - i0 - 1
        circum = np.max((1, 8*level))
        quadrant = (angle // (circum // 4)) %4 
        pos = angle % (circum // 4) 
        if quadrant == 0:
            x = maxpos
            y = pos - level + 1
        elif quadrant == 1:
            x = maxpos - pos - 1
            y = maxpos
        elif quadrant == 2:
            x = - maxpos
            y = maxpos - pos - 1
        elif quadrant == 3:
            x = pos - level + 1
            y = -maxpos
        return int(x), int(y)


    def part2(self,data):
        print("Solution part 2:", 
                self.radial_distance(data) + self.angular_distance(data))
        N = 10
        offset = int(N/2)-1
        lolMatrix = np.zeros((N,N),dtype=int)
        current = 1
        lolMatrix[offset,offset] = current
        i = 1
        np.set_printoptions(suppress=1)
        while current < data:
            x,y = self.get_pos(i)

            mask = np.zeros((N,N),dtype=bool)
            mask[offset+x-1:offset+x+2, 
                 offset+y-1:offset+y+2] = 1

            current = np.sum(lolMatrix[mask])
            lolMatrix[x+offset,y+offset] = current
            print(lolMatrix[:,::-1].T)
            i+=1





if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--test',help='run testfile',
            action ='store_true',default=False)
    parser.add_argument('-p','--part',help='select part',
            choices =[1,2],default=1, type=int)
    args = parser.parse_args()

    day3 = Day3(test = args.test)
    print (day3.solve(part = args.part))
    # import matplotlib.pyplot as plt
    # period = 2
    # i0 = 10
    # for i in range(1, 80):
    #     x,y = day3.get_pos(i)
    #     plt.annotate(str(i), (x,y))
    # plt.axis([-5,5,-5,5])
    # plt.show()


