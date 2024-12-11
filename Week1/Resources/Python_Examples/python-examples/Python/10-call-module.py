#imports user written module.py and give it a different name for use here
import module as m
#Can also import only the person1 dictionary from the module as below. 
#from mymodule import person1
#Commented since above already imported entire module

a = m.person1["age"]
print(a) 

#these are built-in modules
import platform
x = platform.system()
print(x)

#math module with lots of math functions
import math 
x = math.sqrt(81)
y = math.floor(7.7)
z = math.pi
print(x,y,z) 

#regular expression module
import re

txt = "The     rain in Spain"
x = re.search("^The.Spain$", txt) 
#Output interepretation: <re.Match object>: Indicates that the object is a match object returned by the re module.
#span=(0, 17): Indicates the start and end indices of the match within the original string. 
#In this case, the match starts at index 0 and ends at index 17 (exclusive)
# match='The rain in Spain': Shows the actual matched substring, which is "The rain in Spain".

print(x)
# delimiter for splitting the string  is space \s
x = re.split("\s", txt)
print(x) 

# importing sys module that handles command line arguments; 
# be sure to give "3" arguments when running this code
import sys
  
# storing the arguments
program = sys.argv[0]
arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]
  
# displaying the program name
print("Program name : " + program)
  
# displaying the arguments
print("arg1 : " + arg1)
print("arg2 : " + arg2)
print("arg3 : " + arg3)
print("Number of arguments : ", len(sys.argv))
print(sys.argv)


