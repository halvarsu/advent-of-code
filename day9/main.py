from part1 import part1
from part2 import part2

if __name__ == "__main__":
    with open('input') as infile:
        data = infile.read()

    outstring = ''

    test1 = ["ADVENT","A(1x5)BC","(3x3)XYZ","A(2x2)BCD(2x2)EFG",
            "(6x1)(1x3)A","X(8x2)(3x3)ABCY"]

    
    outstring = part1(data)
    with open('output.txt', 'w') as outfile:
        outfile.write(outstring)
    
    print 'Length of decomp 1:', len(outstring.strip(' ').strip('\n'))
    print 'Length of decomp 2:', part2(data)
    'test 1: 11658395077'
