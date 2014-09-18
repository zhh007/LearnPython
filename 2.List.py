
x = list('Hello')
print(x)


y = "".join(x)
print(y)


x = [1, 1, 1]
x[1] = 2
print(x)


names = ['Void', 'Alice', 'Jack']
del names[1]
print(names)

name = list('Perl')
name[2:] = list('ar')
print(name)

list1 = [1, 2, 3]
list1.append(4)
print(list1)

x = [1, 2, 1, 3]
print(x.count(1))


a = [1, 2, 3]
b = [4, 5]
a.extend(b)
print(a)

a = ['love', 'for', 'good']
print(a.index('for'))


a = [1, 2, 3]
a.insert(1, 'b')
print(a)


x = [1, 2, 3]
y = x.pop()
print(y)


x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('be')
print(x)


x = [1, 2, 3]
x.reverse()
print(x)


x = [4, 5, 8, 9, 2, 1, 7]
x.sort()
print(x)

