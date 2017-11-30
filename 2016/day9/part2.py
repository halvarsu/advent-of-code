from part1 import part1

def get_markers(string):
    '''finds all markers and counts amount and count recursively'''
    i = 0
    outcount = 0
    while i < len(string):
        marker = False
        if string[i] == '(':
            x = string.find('x',i)
            mstop = string.find(')',i)
            try:
                r_amount = int(string[i+1:x])
                r_count = int(string[x+1:mstop])
                marker = True
            except ValueError:
                r_count = 1
                r_amount = 1
                marker = False
        if marker:
            r_domain = string[mstop+1:mstop+r_amount+1]
            outcount += r_count*get_markers(r_domain)
            i = mstop+r_amount+1
        else:
            outcount+=1
            i += 1
    return outcount

def part2(data):
    return get_markers(data)

if __name__ == "__main__":

    test = ["(3x3)XYZ", "X(8x2)(3x3)ABCY",
            "(27x12)(20x12)(13x14)(7x10)(1x12)A",
            "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"]
    i = 2
    print get_markers(test[i])#part2(test[i])

