# import os

# root_dir = './references_revised/'

# dirnames = [] # collect all category directories in this list
# fnList = [] # collect all filenames in this list
# output = [] # collect all UNIQUE filenames in this list

# for refdirname, refdirnames, reffilenames in os.walk(root_dir):
# 	dirnames.append(refdirname)

# dirnames = dirnames[1:] # remove root directory from directory list, only include subfolders (which are the categories)


# for dr in dirnames:
# 	for rdname, rdnames, fns in os.walk(dr):
# 		fnList.append(fns) # add all lists of filenames per category to the list

# fnList = [item for sublist in fnList for item in sublist] # flatten the list so we just have a list of all audio filenames

# print len(fnList)

# for x in fnList:
#     if x not in output:
#         output.append(x) # make a copy of the filename list containing only unique filenames

# print len(output) # number of unique named audio files

import os
cpt = (files for r, d, files in os.walk("./references_revised/"))
mylist = []

for f in cpt:
	mylist.append(f)

print len(mylist)