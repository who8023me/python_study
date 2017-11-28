#!/usr/bin/python
#Filename:backup_ver1.py
import os
import time
#1.The files and directories to be backed up are specified in a list
source=['/home/simon/git_hub/python_study','/home/simon/git_hub/cpp_study']
#if you are using windows,use soruce=[r'C:\Documents',r'D:\Work']or something like that 
#2.The backup must be stored in a main backup directory
target_dir='/mnt/'
#3.The files are backed up into a zip file
#4.The name of zip archive is the current date and time
target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'
#5.We use the zip command (in Unix/Linux) to put the files in a zip archive
zip_command="zip -qr '%s' %s"%(target,' '.join(source))
#Run the backup
if os.system(zip_command)==0:
	print 'Successful backup to',target
else:
	print 'Backup FAILED'

