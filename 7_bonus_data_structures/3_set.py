# CRUD (create, remove, update, delete)

s = set()

s.add('1')
s.add('2')
s.add('3')
s.add('1')
s.add('1')

print(s)
print('pop el ->', s.pop())
print('len -> ', len(s))

# delete
# del s
# print(s)

# Для чего использовать?

# Inititate
s1 = {1,2,3,4}
s2 = {3,4,5,6}

# Intersection
print(s1.intersection(s2))

# Difference
print(s1.difference(s2))
print(s2.difference(s1))
