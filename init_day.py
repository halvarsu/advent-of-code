import sys, glob, os

try:
    day = int(sys.argv[1])
except IndexError, ValueError:
    print "Bad usage, needs day as int arg"
    sys.exit(1)


folder = 'day%d' % day
if not glob.glob(folder):
    os.system('mkdir %s' %folder)
    with open('dayXX.py') as infile:
        with open('%s/day%d.py' %(folder,day),'w') as outfile:
            outfile.write(infile.read().replace('XX', '%d' %day))
else:
    print 'Folder %s already exists. exiting' %folder
    sys.exit(1)

print day
