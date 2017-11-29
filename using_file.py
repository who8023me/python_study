#!/usr/bin/python
#Filename:using_file.py
poem='''\
Programming is fun 
When the work is done
if you wanna make you work also fun:
use Python!
'''
f=file('poem.txt','w')#open for "w"riting
f.write(poem)#write text to file
f.close()#close the file
f=file('poem.txt')
#if no mode is specified.'r'ead mode is assumed by default
while True:
	line=f.readline()
	if len(line)==0:#zero length indicates EOF
		break
	print line,
f.close()#close file
