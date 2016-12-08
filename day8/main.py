import numpy as np

def shift(current, c):
    n = len(current)
    new = np.zeros_like(current)
    for i in range(n):
        new[i] = current[(i-c)%n]
    return new


def rotate(screen, axis, num, c):
    if axis in ['row', 0, 'y']:
        print num
        screen[num] = shift(screen[num],c)
    elif axis in ['column',1,'x']:
        screen[:,num] = shift(screen[:,num],c)
    return screen

def rect(screen, A, B):
    screen[:B,:A] = 1
    return screen

def to_string(screen):
    screenstring = '_'*(screen.shape[1]+2)+'\n'
    screenstring += '|'+' '*screen.shape[1]+'|\n'
    for row in screen:
        screenstring+='|'
        for i in row:
            screenstring+='#' if i else ' '
        screenstring += '|\n'
    screenstring += '|'+'_'*screen.shape[1]+'|\n'
    
    return screenstring

def total(screen):
    return np.sum(np.sum(screen))

if __name__ == "__main__":
    with open('input') as infile:
        cmds = map(str.split, infile.readlines())
        screen = np.zeros((6,50), dtype='int')
        for cmd in cmds:
            if cmd[0] == 'rotate':
                axis = cmd[1]
                num = int(cmd[2].split('=')[1])
                c = int(cmd[-1])
                screen = rotate(screen, axis,num,c)
            elif cmd[0] == 'rect':
                A,B = map(int, cmd[1].split('x'))
                screen = rect(screen, A, B)

    print screen


    print to_string(screen), total(screen)
