#usr/bin/python3
#inport the module of the user math functions

import os
import sys
import windice as wd
import lindice as ld

#Main code 
#Определение типа операционной системы (windows = nt, linux = posix))

#try:
switch = True
if (os.name == 'posix'):
	os.system('python3 lindice.py')
elif (os.name == 'nt'):
	os.system('python3 windice.py')
else:
	print('This OS in not supported!')		
	switch = False
	
	
#except ValueError:
#    print("You have some mistake of userinput Value!")
#except TypeError:
#   print("You have some mistake of type Value!")
#except SystemError:
#	print("This is system mistake! Please don't panic! Relax!")
#except FileNotFoundError:
#   print("Thereis't file here!")
#except FileExistsError:
#   print("File or dyrectory allready exist!")
#except ImportError:
#	print("Some modules not loaded, please check your source code!")
#except IOError:
#	print('An error IO file!')	

