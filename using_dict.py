#!/usr/bin/python
#Filename:using_dict.py
#'ab' is short for 'a'dress'b'ook
ab={'Swaroop':'swaroopch@byteofpython.info',
'Larry':'lary@wall.org',
'Matsumoto':'matz@ruby_lang.org',
'Spammer':'spammer@hotmail.com'
}
print "Swaroop's address is %s"%ab['Swaroop']
#Adding a key/value pair
ab['Guido']='guido@python.org'
#Deleting a ley/value pair
del ab['Spammer']
print '\nThere are %d contacts in the address-book\n'%len(ab)
for name,address in ab.items():
	print 'Contact %s at %s'%(name,address)
if 'Gudio' in ab:#OR ab.has_key("Gudio')
	print"\nGudio's address is %d"%ab['Gudio']

