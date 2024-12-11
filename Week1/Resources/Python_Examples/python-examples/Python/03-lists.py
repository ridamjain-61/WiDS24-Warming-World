#Lists use Square brackets
#List allow duplicate values
mylist = ["apple", "banana", "cherry", 32, "apple", 6, 2.5]
print("0", mylist)
print("1", len(mylist))

#List items are indexed, first index starts at 0
print("2", mylist[2])
#negative measns start from end
print("3", mylist[-1])
print("4", mylist[3:6])

#List items are mutable i.e. can be changed
#last index is not included, it changes for 1 and 2 i.e. banana and cherry
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["mango", "watermelon"]
print("5", thislist)

#Can insert more items than specified by index
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print("6", thislist) 

#can inser less items than specified
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print("7", thislist) 

#can insert without replacement via insert method
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
thislist.append("orange")
print("8", thislist)

#can remove items as well
thislist.remove("orange")
#pop is used to remove from specific index
thislist.pop(1)
print("9", thislist)
#no argument, removes last element
thislist.pop()
#can use del also
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print("10", thislist)
#removes entire list
del thislist

#List comprehension
#newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print("11", newlist) 
newlist = [x.upper() for x in fruits] 
print("12", newlist) 


#Join lists; + creates a new list; while extend, extends the first list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print("13", list3) 

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print("14", list1) 


#Few other methods
#sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print("15", thislist)
#descending sort
thislist.sort(reverse = True)
print("16", thislist)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
#reverses current order
thislist.reverse()
print("18", thislist)

#copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print("19", mylist)
