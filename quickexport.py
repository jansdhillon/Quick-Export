import os, glob, shutil

#get path for quick export folder
folder = os.path.join(os.path.join(os.path.expanduser('~')), 'Quick Export')
#extract files
files = glob.glob(os.path.join(folder, '*'))

#copy files to OneDrive folder and delete from quick export folder
while len(files) > 0:
    file = files.pop()
    name = os.path.basename(file)
    if (os.path.isfile(file)) and (name != 'quickexport.py'):
        shutil.copy(file, os.path.join(os.path.join(os.path.expanduser('~')), 'OneDrive - UBC/Resumes and CL (OneDrive)'))
        os.remove(file)