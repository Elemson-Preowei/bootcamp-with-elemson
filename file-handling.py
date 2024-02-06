# fp = open("modules-packages.py", "w")
# print(fp.readline())
# print(fp.readline())
# print(fp.readline())
# fp.close()
# print(fp.readline())

"""
# Assingment
using python create a file called file.txt
and add the following content
- this is the first line of the file
- this is the second line of the file
"""

# with open("modules-packages.py") as fp:
#     for line in fp:
#         print(line)
#     """
#     This code works, the issue was that the file `modules-packages.py`
#     had no content that was why we were not getting anything printed out

#     What happened is that there was a time we opened that file with the `w` 
#     mode, when you open an already existing file in `w` mode it will clean the
#     old content. So that was how the content I was expecting to print was lost.
#     But I have sorted it out this morning.
#     """
# with open("modules-packages.py") as fp:
#     n = 1
#     for line in fp:
#         print(n, line.rstrip("\n")) # strip off the line return
#         n += 1
#     """
#     Here I have used the `rstrip` command to remove the return command that
#     always print a new line. 
#     You can run both and see the difference
#     """

import os

# working directories from inside python - listing the content of a directory

content_dir = os.listdir('../bootcamp-with-elemson/')
for dir in content_dir:
    print(dir)

with os.scandir('.') as dirs:
    for dir in dirs:
        print(dir.name)

# listing only the general files of a directoryand excluding any sub-directory

for item in os.listdir('.'):
    if os.path.isfile(os.path.join('.', item)): # ./.git will be excluded because it is not a regular file
        print(item)

with os.scandir('.') as items:
    for item in items:
        if item.is_file():
            print(item.name)

# git fetch upstream/master
# git checkout master
# git merge upstream/master
# git checkout elemson
# git merge origin/master
