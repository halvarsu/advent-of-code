import hashlib
pw = 'wtnhxymk'

base =  b'wtnhxymk'#b'abc'
m = hashlib.md5()
m.update(base)
print (m.hexdigest())

i = 0
integers = []

valid_pos = '01234567'

pw = ['_']*8
print (pw)
print (''.join(pw))

while len(integers)<8:
    m2 = m.copy()
    m2.update(b'%d'%i)
    a = m2.hexdigest()
    if a[0:5]=='00000':
        if a[5] in valid_pos and pw[int(a[5])]=='_':
            integers.append(i)
            #print (a[6], i)
            pw[int(a[5])]=a[6]
            status = ''.join(pw)
            status = status + '\b'*(len(status)+1)
            print (status,)
    i+=1

print (integers)
