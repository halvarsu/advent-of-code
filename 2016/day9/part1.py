def part1(data):
    outstring = ''
    i=0
    while i < len(data):
        marker = False
        if data[i] == '(':
            x = data.find('x',i)
            mstop = data.find(')',i)
            try:
                r_amount = int(data[i+1:x])
                r_count = int(data[x+1:mstop])
                marker = True
            except ValueError:
                r_count = 0
                r_amount = 0
                marker = False
        if marker:
            outstring += data[mstop+1:mstop+r_amount+1]*r_count
            i = mstop + r_amount + 1
        else:
            outstring += data[i]
            i += 1
    return outstring

