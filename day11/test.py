a = ['1','2','3','4']

c = ['1']
b = [i if i in c else "g" for i in a ]
print b
