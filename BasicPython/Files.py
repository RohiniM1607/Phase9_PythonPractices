myobj = open("TestFile.txt", 'w')
print(myobj.write("Hey I have started using files in Python\n"))
myobj.close()

myobj = open("TestFile.txt", 'w')
marks = 58
print(myobj.write(str(marks)))
myobj.close()

myobj = open("TestFile.txt", 'w')
lines = ["Hello everyone\n",
    "Writing multiline String\n",
    "This is the #third line"
]
myobj.writelines(lines)
myobj.close()

#Reading from file
myobj = open("TestFile.txt", 'r')
var = myobj.read()
print(var)
myobj.close()

myobj = open("TestFile.txt", 'r')
var = myobj.readlines()
print(var)
myobj.close()

myobj = open("TestFile.txt", 'r')
var = myobj.readlines()
for line in var:
    words = line.split()
    print(words)

myobj = open("TestFile.txt", 'r')
var = myobj.readlines()
for line in var:
    words = line.splitlines()
    print(words)

myobj = open("TestFile.txt", 'r')
for str in myobj:
    print(str)
myobj.close()

myobj = open("TestFile.txt", 'r')
str = myobj.read()
print(str)
print("Initially, the position of the file object is: ", myobj.tell())
myobj.seek(0)