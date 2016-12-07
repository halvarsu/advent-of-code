def ABAs(s):
    l = []
    for i in range(len(s)-2):
        if s[i]==s[i+2] and s[i]!=s[i+1]:
            l.append(s[i:i+2])
    return l


inp =[ "aba[bab]xyz", "xyx[xyx]xyx","aaa[kek]eke","zazbz[bzb]cdb" ]
s = 0

with open('input') as infile:
    for line in infile:
        success = False
        sline = line.strip('\n')
        start = [x for x,v in enumerate(sline) if v=='[']
        stop =  [x for x,v in enumerate(sline) if v==']']
        slist = [sline[:start[0]]]\
                    +[sline[b+1:a] for a,b in zip(start[1:],stop[:-1])] \
                    +[sline[stop[-1]+1:]]
        supernet = '. _'.join(slist)
        hypernet = '. _'.join([sline[a+1:b] for a,b in zip(start,stop)])

        superABAs = ABAs(supernet)
        hyperABAs = ABAs(hypernet)
        for sABA in superABAs:
            sBAB = sABA[::-1] 
            if sBAB in hyperABAs:
                success = True
        s += success

print s
