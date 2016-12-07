
def ABBA(s):
    for i in range(len(s)-3):
        if s[i:i+2] == s[i+3:i+1:-1]:
            if s[i] == s[i+1]:
                return 0
            else:
                return 1
    return 0

inp = ['abba[mnop]qrst','abcd[bddb]xyyx',"aaaa[qwer]tyui",
        'ioxxoj[asdfgh]zxcvbn']

s = 0
with open('input') as infile:
    #infile= inp
    for line in infile:
        success = False
        sline = line.strip('\n')
        codestarts = [x for x,v in enumerate(sline) if v=='[']
        codestops =  [x for x,v in enumerate(sline) if v==']']
        for a,b in zip(codestarts,codestops):
            if ABBA(sline[a+1:b]):
                success = False
                break
            elif not success and (ABBA(sline[:a]) or ABBA(sline[b+1:])):
                success = True
        print sline, success
        s += success

print s
