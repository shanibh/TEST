import os
import re
import os.path
import sys
def gets_files():
	from os import listdir
	from os.path import isfile, join
	dir_path = os.path.dirname(os.path.realpath(__file__))
	onlyfiles = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
	return onlyfiles

def count_lines(x):
	try:
		file_obj = open(x,"r")
		file_cont = file_obj.read()
		split_file = re.split("(?<=[ .!?\n\t]) +",file_cont)
		return len(split_file)
	except ValueError:
		print("Oops, the file is not exist")
			

def read_file(x):
	try:
		file_obj = open(x,"r")
		file_cont = file_obj.read()
		split_file = re.split("/([^.]*)\.(.*)/",file_cont)
		for tmp in split_file:
			print(tmp)
	except ValueError:
		print("Oops, the file is not exist")

def create_file(name,content):
	try:
		f = open(name,"w+")
		f.write(content)
		f.close()
	except ValueError:
		print("Oops, the file is not exist")


def main():
	 print(os.path.basename(__file__)+" counts the lines of code")
	 l=0
	 n=0
	 s=0
	 listfiles = gets_files()
	 for x in listfiles:
		 counter=count_lines(x)
		 print(x+": "+str(counter))
		 read_file(x)
		 n=n+1
		 s=s+counter
	 print("%d files in total, with %s lines in total" % (n,s))
	 create_file(sys.argv[1],sys.argv[2])



if __name__ == "__main__":
	main()
