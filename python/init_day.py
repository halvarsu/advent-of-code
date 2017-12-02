import sys, glob, os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('day',type=int)
args = parser.parse_args()



folder = 'day' + str(args.day)

if glob.glob(folder):
    print('Folder {} already exists. exiting'.format(folder))
    sys.exit(1)

os.system('mkdir {}'.format(folder))
with open('dayXX.py') as infile:
    with open('{}/day{}.py'.format(folder,args.day),'w') as outfile:
        outfile.write(infile.read().replace('XX', str(args.day)))

print("Folder day{} initialized".format(args.day))
