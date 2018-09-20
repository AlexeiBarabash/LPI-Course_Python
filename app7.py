#!/usr/bin/env python3


file_name = input("What filename you want : ")
path = input("please input the full path or . dont wirte / in the end: ")

with open(path+"/"+file_name,'w') as file:
	
	line = input("Please enter a word to add to file : ")
	file.write(line+"\n")
	
	while line != "":	
			
		line=input("Please enter a word to add to file : ")
		file.write(line+"\n")  
		  
	file.close()
