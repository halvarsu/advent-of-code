import hashlib
pw = 'wtnhxymk'

base =  b'wtnhxymk'#b'abc'
m = hashlib.md5()
m.update(base)
print (m.hexdigest())

i = 0
integers = []


while len(integers)<8:
    m2 = m.copy()
    m2.update(b'%d'%i)
    if m2.hexdigest()[0:5]=='00000':
        integers.append(i)
        print (m2.hexdigest()[5], i)
    i+=1

print (integers)
