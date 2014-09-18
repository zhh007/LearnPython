
phone = {'a': 124, 'b':456, 'c':789}
print(phone['a'])

print(len(phone))


phone['a'] = 1
print(phone)

del phone['b']
print(phone)

if 'a' in phone:
	print('a is here.')

for k, v in phone.items():
	print('%s = %s' % (k, v))




