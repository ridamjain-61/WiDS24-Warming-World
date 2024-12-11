#Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and 
# do not allow duplicates.

#Dictionaries are written with curly brackets, and have keys and values:

thisdict ={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("0", thisdict)
print("1", thisdict["brand"])
print("2", len(thisdict))
print("3", type(thisdict)) 

#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

#Duplicate values will overwrite existing values:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print("4", thisdict) 
#Can change values
thisdict["year"] = 2023
thisdict.update({"year": 2024}) 
print("5", thisdict)


#access items
x = thisdict["model"]
print("6", x)
x = thisdict.get("model")
print("7", x)
x = thisdict.keys() 
print("8", x)
x = thisdict.values() 
print("9", x)
x = thisdict.items() 
print("10", x)
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") 


#can add more items, both work
thisdict["color"] = "white"
thisdict.update({"gear": "auto"}) 
print("11", thisdict)


#can remove items; pop removes the item, popitem removes last item
thisdict.pop("model")
thisdict.popitem()
print("12", thisdict) 

#can copy
mydict = thisdict.copy()
print("13", mydict)

#Can create nested dictionaries
child1 = {
  "name" : "Ravi",
  "year" : 2004
}
child2 = {
  "name" : "Rekha",
  "year" : 2007
}
child3 = {
  "name" : "Ranjith",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 

print("14", myfamily)
