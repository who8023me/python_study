#!/usr/bin/python
#Filename:class_init.py
class Person:
	def __init__(self,name):
		self.name=name;
	def sayHi(self):
		print 'Hello,my name is',self.name
p=Person('simon')
p.sayHi()
#This short example can also be written as Person('simon').sayHi()

