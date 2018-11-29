import os
print(os.getcwd())#Returns the current working directory.
#os.mkdir('junkdir')#Create a directory named path with numeric mode mode.
print(os.listdir(os.curdir)) #Return a list of the entries in the directory given by path.
print('junkdir' in os.listdir(os.curdir))
#os.rename('junkdir', 'foodir')#Rename the file or directory src to dst.
print('junkdir' in os.listdir(os.curdir))
print('foodir' in os.listdir(os.curdir))
#os.rmdir('junkdir') #Remove (delete) the directory path.
fp = open('junk.txt', 'w')
fp.close()
print('junk.txt' in os.listdir(os.curdir))
os.remove('junk.txt')
print('junk.txt' in os.listdir(os.curdir))

