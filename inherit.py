#!/usr/bin/python
#Filename:inherit.py
class SchoolMember:
	'''Represents and school memeber'''
	def __init__(self,name,age,):
		self.name = name
		self.age = age
		print '(Initialized SchoolMember:%s)'%self.name
	def tell(self):
		'''Tell my details.'''
		print 'Name:"%s"Age:"%s"'%(self.name,self.age),
class Teacher(SchoolMember):
	'''Represents a teacher.'''
	def __init__(self,name,age,salary):
		SchoolMember.__init__(self,name,age)
		self.salary=salary
		print '(Initialized Teacher:%s)'%self.name
	def tell(self):
		SchoolMember.tell(self)
		print 'Salary %d'%self.salary
class Student(SchoolMember):
	'''Represents a student.'''
	def __init__(self,name,age,marks):
		SchoolMember.__init__(self,name,age)
		self.marks=marks
		print '(Initialized Student:%s)'%self.name
	def tell(self):
		SchoolMember.tell(self)
		print 'marks %d'%self.marks
t=Teacher('Mrs.simon',40,30000)
s=Student('jia',22,75)
print #Prints a blank line
members = [t,s]
for member in members:
	member.tell()#works for both teachers and Students
	
