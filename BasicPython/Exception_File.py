try:
    fh = open("TestFile.txt", "w")
    try:
        fh.write("This is my test file for exception handling")
    finally:
        print("Going to close the file")
        fh.close()

except IOError:
    print("Error: Can't find file to write the data")
else:
    print("I will execute when no exception occurs")
finally:
    print("I am always executing")


try:
    num = int(input("Enter a positive integer: "))
    if(num<=0):
        ValueError("This is a negative number")
        #print(num)
except ValueError as e:
    print(e)