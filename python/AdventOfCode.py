import glob, urllib

class AdventOfCode(object):

    """Docstring for AdventOfCode. """

    def __init__(self, day, filename):
        """TODO: Basic superclass for AdventOfCode 2016

        :day: Day number
        :filename: filename of inputfile

        """
        self._day = day
        self._filename = filename
        
    def download_input(self):
        # Has problems because of authentication... 
        # Probably wont bother fixing
        return NotImplementedError
        url  = "http://adventofcode.com/2016/day/%d/input" %(self.get_day())
        filename = self.get_filename()
        print( "Opening %s" %url)
        with open(filename,'w') as outfile:
            # write data from url to file 
            map(outfile.write, urllib2.urlopen(url))

    def get_filename(self):
        return self._filename

    def set_filename(self, filename):
        self._filename = filename

    def get_day(self):
        return self._day

    def set_day(self, day):
        self._day = day

    def get_input(self, filename = None):
        if filename is None:
            filename = self.get_filename()

        if not glob.glob(filename):
            raise IOError('File %s doesnt exist' % filename)
            #self.download_input()
        with open(filename) as infile:
            data = self.input_prosessor(infile)
        return data

    def solve(self, part):
        raise NotImplementedError
    
    def input_prosessor(self, infile):
        """Should prosess input into wanted format.
        example: 
            return map(int,infile)"""
        raise NotImplementedError 

def partition(l, p):
    return reduce(lambda x, y: x[not p(y)].append(y) or x, l, ([], []))

def sign(x):
    if x>= 0:
        return 1
    else:
        return -1

def representsint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
