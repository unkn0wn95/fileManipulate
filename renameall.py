import os

#put outside folder 
path = os.chdir("j") #name of the file

i = 0

for file in os.listdir(path):
	new_file_name = "01{}.txt".format(i)
	os.rename(file,new_file_name)
	i = i+1
