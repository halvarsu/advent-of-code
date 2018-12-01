p=print
f=list(map(int,open('input')))
p(sum(f))
s=0
w=set()
for n in f:
 s+=n
 if s in w:break
 w.add(s);f.append(n)
p(s)
