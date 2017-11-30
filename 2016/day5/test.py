import hashlib
integers =[3231929, 5017308, 5278568, 5357525, 5708769, 6082117, 8036669,
            8605828]
integers = [2231254, 2440385, 2640705, 3115031, 5045682, 8562236, 9103137, 9433034]
base = b'wtnhxymk'
m = hashlib.md5()
m.update(base)

for i in integers:
    m2 = m.copy()
    m2.update(b'%d'%i)
    print (m2.hexdigest()[5])

