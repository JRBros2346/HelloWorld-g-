#Build script for main
import os

#Get a list of all the .cpp files.
cppFilenames=''
for (root,dirs,files) in os.walk(os.getcwd()):
    for file in files:
        if file.endswith('.cpp'):
            cppFilenames+=' '+root+'/'+file

print("Files:",cppFilenames)

assembly='main'
compilerFlags='-g'
#'-Wall -Werror'

print("Building %s..."%assembly)
os.system('g++ %s %s -o %s.exe'%(cppFilenames,compilerFlags,assembly))
