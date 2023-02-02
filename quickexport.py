import os, glob, shutil

folder = os.path.join(os.path.join(os.path.expanduser('~')), 'Quick Export')
files = glob.glob(os.path.join(folder, '*'))

while len(files) > 0:
    file = files.pop()
    if os.path.isfile(file):
        
        shutil.copy(file, os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop'))
        os.remove(file)