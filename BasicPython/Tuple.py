myTuple = (10,20,30,[1,2,3])
print(type(myTuple[3][0]))

print(id(myTuple))
myTuple = (100,)+myTuple[1:]
print(myTuple)
print(id(myTuple))

addr = 'monty@python.org'
uname, domain = addr.split('@')
print(uname)
print(domain)
print(type(addr))
print(type(uname))
print(type(domain))