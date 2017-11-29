#!/usr/bin/python
#Filename:objvar.py
class Person:
	'''Represents a person.'''
	population = 0
	def __init__(self,name):
		'''Initializes the person's data'''
		self.name = name;
		print '(Initializing %s)'%self.name
	#When this person is created he/she 
	#adds to the population
		Person.population+=1
	def __del__(self):
		''' I am dying'''
		print '%s says bye.'%self.name
		Person.population -= 1
		if Person.population == 0:
			print ' I am the last one.'
		else:
			print 'There are still %d people left.'%Person.population
	def sayHi(self):
		'''Greeting by the person.
Really,that's all it dose.'''
		print 'Hi my name is %s'%self.name
	def howMany(self):
		'''Prints the current population.'''
		if Person.population == 1:
			print 'I am the only person here.'
		else:
			print 'We have %d persons here.'%Person.population
simon=Person('simon')
simon.sayHi()
simon.howMany()
peter=Person('peter')
peter.sayHi()
peter.howMany();
simon.sayHi()
simon.howMany()	

