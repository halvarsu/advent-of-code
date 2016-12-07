from operator import itemgetter


with open('test') as infile:
    names =[]; ids = []; checksums=[]
    for line in infile.readlines():
        sline = line.split('-')
        names.append(''.join(sline[:-1]))
        rest = sline[-1][:-1].replace(']','').split('[')
        ids.append(rest[0])
        checksums.append(rest[1])

valid = []

s = 0
for i, name in enumerate(names):
    letters = list(sorted(set(name)))
    lcount = [name.count(l) for l in letters]
    print lcount
    countsort = [x[0] for x in sorted(enumerate(lcount),key=itemgetter(1))][::-1]
    code = ''.join([letters[j] for j in countsort[:5]])
    print code
    if code == checksums[i]:
        s+=int(ids[i])

print s
