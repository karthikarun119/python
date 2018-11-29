import os
import pbs,sys
import glob
fp = open('junk.txt', 'w')
fp.close()
a=os.path.abspath('junk.txt')
print(a)
lis=os.path.split(a)
print(lis[0])
print("directory name=====%s"%os.path.dirname(a))
print("Filename=====%s"%os.path.basename(a))
lis1=os.path.splitext(os.path.basename(a))
print("filename split ",lis1)
print("path exist ",os.path.exists(lis[0]))
print("path exist ",os.path.isfile(lis[0]))
print("directory exist",os.path.isdir(a))
print(os.path.expanduser('~/local'))
print(os.path.join(os.path.expanduser('~'), 'local', 'bin'))
print(os.system('ls'))

for dirpath, dirnames, filenames in os.walk(os.curdir):
    for fp in filenames:
        print( os.path.abspath(fp))

#print(os.environ.keys())
print(glob.glob('*.py'))
print(sys.platform)
print(sys.version)
print(sys.prefix)
print(sys.argv)
print(sys.path)
import pickle

l = [1, None, 'Stan']

pickle.dump(l, file('test.pkl', 'w'))

print(pickle.load(file('test.pkl')))

