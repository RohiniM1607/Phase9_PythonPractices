dict1 = {}
dict1 = {1:'AFBC',2:'DEF',3:'GHI',4:'JKL'}
dict1 = {1:'CSE', 'Name': 'Rohini', 'List':[1,2,3], 'tuple': (10,20)}
print(type(dict1[1]))


print(dict())
numbers = dict(x=5, y=0)
print(numbers)
numbers1 = dict({'x':4, 'y':5})
print(numbers1)
numbers1 = dict([('x', 5), ('y', -5)])
print(numbers1)

dict ={'name':'Arul Kumar', 'age': 35, 'mail': 'arul@gmail.com'}
print(dict['age'])
print(dict['mail'])
print(dict.pop('name'))
print(dict)
print(dict.popitem())
print(dict)

thisdict = {"brand": "Ford", "model": "Mustang"}
print(thisdict)
for x in thisdict:
    print(x, thisdict[x])

d = {1:'one', 2: 'three'}
d1={2:'two'}
d.update(d1)
d2 = {3:'three'}
d.update(d2)
print(d)

