'''listdir()
path.join()
getmtime()
search through a directory
verify txt files
print the files with timestamps
'''

import os


fName = 'file9'

fPath = 'D:\\Work\\GitHub\\python_projects\\script_assignment_directory\\'


abPath = os.path.join(fPath, fName)
print(abPath)
