import shutil
import os
from pathlib import Path

os.chdir('/Users/arun/PycharmProjects/automate-boring-stuff')
for index, filename in enumerate(os.listdir(), start=1):
    print(index, filename)
    
print(f'Path: {Path.home()}')

for folderName, subFolders, fileNames in os.walk(os.getcwd()):
    if 'private' in folderName:
        print("I'm not going to display the contents for this folder... ")
        continue
    
    print(f'======  {folderName}  =============')
    print(f'Subfolders: {subFolders}')
    print(f'Files: {fileNames}')
    
    
    
