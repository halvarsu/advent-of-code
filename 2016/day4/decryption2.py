import numpy as np
import re

with open('input') as infile:
    lines = infile.readlines()
min_length = 200
s = 0

def test_line(line):
    sline = re.split(r'[-\[]',line.strip(']\r\n'))
    name = ''.join(sline[:-2])
    number = int(sline[-2])
    checksum = sline[-1]

    letters = list(sorted(set(name)))
    lcount = [name.count(l) for l in letters]
    ordering = [''] * (max(lcount)+1)
    
    for l,c in zip(letters,lcount):
        ordering[c] += l
    for i in range(len(ordering)):
        ordering[i] = sorted(ordering[i])
    code = ''
    for word in ordering[::-1]:
        for c in word:
            code += c
            if len(code) >4:
                break
        if len(code)>4:
            break
    print code

    if code == checksum:
        return name, number
    else:
        return '',0



def real_name(s, n):
    print n, s
    return ''.join([str(unichr((ord(c)-97+n)%26+97)) for c in s])
    

names = []
numbers = []
for line in lines:
    name, number = test_line(line)
    if name:
        s+=number
        names.append(real_name(name,number))
        numbers.append(number)

print (s)
print names

i = names.index('northpoleobjectstorage')
print numbers[i]

#with open('real_names','w') as outfile:
    #for n in names:
        #outfile.write(n+'\n')
