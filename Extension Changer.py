import os
import fnmatch, re
import glob
files = glob.glob('*.mkv')
for file in files:
	name1 = list(file)
	name2 = []
	i = 0
	while i<= len(name1) - 5:
		name2.append(name1[i])
		i+=1
	name = ''.join(name2)
	new_name = '{}.mp4'.format(name)
	os.rename(file, new_name)