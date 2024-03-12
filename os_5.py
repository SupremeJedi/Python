import os


os.chdir(r'C:\Users\saksh')


for dirpath,dirnames,filenames in os.walk(r'C:\Users\saksh'):
    print('Current Path:', dirpath)
    print('Directories', dirnames)
    print('Files', filenames)
    print()


