# CRUD (create, remove, update, delete)

d = {}
d['key'] = 'value'
d['key'] = 'new_value'
del d['key']
del d

# Iterate
d = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '0': 'zero'}

for i in d:
    print(i)

print("-----------------")

for k in d.keys():
    print(k)

print("-----------------")

for v in d.values():
    print(v)

print("-----------------")

for i in d.items():
    print(i)

print("-----------------")

for k,v in d.items():
    print(k, v)

print("-----------------")

# Unordered
# Справедливо для работы с большими словарями
# https://www.quora.com/Are-Python-dictionaries-unordered
