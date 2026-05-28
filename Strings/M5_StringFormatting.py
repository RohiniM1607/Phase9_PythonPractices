words = input("Enter the String:").split()
n=len(words)
for i in range(0,n):
   print("{} {} {}".format(words[i], words[(i+1)%n], words[(i+2)%n]))
