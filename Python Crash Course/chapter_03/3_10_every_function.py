mylist = ['dog', 'cat', 'monkey']

mylist.remove('monkey')
mylist.append('pig')
mylist.pop()
del mylist[0]
mylist.insert(0,'dog')

print(sorted(mylist))
print(mylist)
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)
print(str(len(mylist)))