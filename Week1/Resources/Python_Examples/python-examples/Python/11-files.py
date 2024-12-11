#read a file
f = open("file.txt","r")
#prints all content
print(f.read())
f.close()


f = open("file.txt","r")
#print first 2 characters
print(f.read(2)) 
f.close()

f = open("file.txt","r")
#prints first line
print(f.readline())
#prints second line
print(f.readline())
f.close()

f = open("file.txt", "r")
for x in f:
  print("for", x) 
f.close() 

#Note I am using a different file file1.txt
#write to file, w overwrites the content, 
#a appends the content
f = open("file1.txt", "a")
f.write("Now the file has some content!")
f.write("Now the file has more content!")
f.close()
f = open("file1.txt","r")
print(f.read())
f.close()



# python3
