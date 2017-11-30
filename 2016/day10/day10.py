import sys, re
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__)  )  )  )
from AdventOfCode import AdventOfCode, partition

class Day10(AdventOfCode):

    """Docstring for Day10. """

    def __init__(self, filename ='input'):
        """TODO: to be defined1.

        :filename: TODO

        """
        AdventOfCode.__init__(self, filename = filename, day=10)

        self._filename = filename
        self.botvals = {}
        self.botinst = {}


    def get_args(self, line):
        return

    def input_prosessor(self, infile):
        for line in infile:
            cmds = re.findall(r'[\w]+ \d+', line)
            if cmds[0].startswith('value'):
                bot = cmds[1]
                val = int(cmds[0].split()[1])
                self.add_value(bot, val)
            else:
                bot = cmds[0]
                self.botinst[bot] = {'low':cmds[1],'high':cmds[2]}
        return self.botvals, self.botinst

    def get_active(self):
        return filter(lambda x: len(self.botvals[x])>1, self.botvals)

    def add_value(self, bot, val):
        if bot.startswith('output'):
            if bot in self.outputs:
                self.outputs[bot].append(val)
            else:
                self.outputs[bot] = [val]
        if bot in self.botvals:
            self.botvals[bot].append(val)
        else:
            self.botvals[bot] = [val]


    def solve(self):
        self.get_input()
        max_bot = max(sorted(self.botinst.keys()+self.botvals.keys()),
                      key=lambda x:int(x.split()[1]))
        m = int(max_bot.split()[1])

        active = self.get_active()
        while active:
            print active
            bot = active[0]
            inst = self.botinst[bot]
            high = max(self.botvals[bot])
            low  = min(self.botvals[bot])
            self.add_value(inst['low'], low)
            self.add_value(inst['high'], high)
            self.botvals[bot] = []

            print active.pop(active.index(bot))
            if not active:
                active = self.get_active()
            if len(active) > 1:
                print "Two active bots! What to do"
                print active
                break

if __name__ == "__main__":
    day10 = Day10()
    data = day10.solve()

