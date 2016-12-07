aso = 'heisanz'
number = 2
print ''.join([str(unichr((ord(a)-97+number)%26+97)) for a in aso])
