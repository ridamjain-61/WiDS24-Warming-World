#set is written with curly brackets
#Duplicates ignored
thisset = {"apple", "banana", "cherry", "apple", True, 23, 23.0}
print("0", thisset)
print("1", len(thisset)) 
print("2", type(thisset))


#set is a collection which is unordered and unindexed.
#unordered means that the items in a set do not have a defined order.
#Set items can appear in a different order
print("3", thisset)
#You cannot access items in a set by referring to an index or a key 
#but you can loop through via for loop or check if value present
print("4", "banana" in thisset) 

#Cannot change items but can add add/remove items via add/update methods
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print("5", thisset) 

#Can add elements of a set to a set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print("6", thisset) 

#Can add elements of a list to a set as well
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print("7", thisset) 

#remove items
#if item to removed does not exist, remove() will raise an error 
thisset.remove("banana")
#if item to removed does not exist, discard() will NOT raise an error
thisset.discard("mango")

#pop can remove only the last item; Sets are unordered, 
#so when using the pop() method, you do not know which item that gets removed.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print("8", x)
print("9", thisset) 

#sets are like mathematical sets. you can do union, intersection etc. 
#Join sets
#union of two sets;  Both union() and update() will exclude any duplicate items.
#Note union returns a new set, while update updates the first set
set1 = {"a", "b" , "c", "a"}
set2 = {1, 2, 3, 2}
set3 = set1.union(set2)
print("10", set3) 
set1.update(set2)
print("11", set1) 

#interesection, much like union, returns a new set; where as intersection_update updates the first set 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print("12", z) 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print("13", x) 

# symmetric_difference: Return a set that contains all items from both sets, except items that are present in both; 
# where as symm...update updates the first set 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print("14", z)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print("15", x) 

