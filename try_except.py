#!/usr/bin/python
#Filename:try_except.py
import sys
try:
	s=raw_input('Enter something-->')
except EOFError:
	print '\nWhy did you do an EOF on me?'
	sys.exit()#exit the program
except:
	print '\n Some error/exception occured.'
	#here,we are not exiting the program
print 'Done'
