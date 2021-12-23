filename = "input"
with open(filename) as infile:
    txt = infile.read()
y0 = abs(int(txt.split()[-1].split("=")[-1].split("..")[0]))
print((y0*(y0+1))//2)

