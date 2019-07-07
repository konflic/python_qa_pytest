# CRUD (create, remove, update, delete)
l = []
print("Type: ", type(l))

l.append(1)
l.extend([2,3,4])
print("l -> ", l)

l[0] = "One"
l.insert(1, 103)
print("len of l -> ", len(l))
print("l -> ", l)

del l[0]
print("l -> ", l)

print("3 in l -> ", l.count(3), "times")
print(l.pop(), l) # index or last

# del l
# print("l -> ", l)

# Comprehension
# l = [x for x in range(50) if x % 2 == 0]
# print(l)

# Slice
# l = [x for x in range(50) if x % 2 == 0]

# Iterate
# l = [1,2,3,4,5]
# for i in l:
#     print(i)

# # Copy list
# l1 = [1,2,3]
# l3 = l1
# l3.extend(['+', '+', '+'])
# print(l1)
# # First copy option
# l3 = l1.copy()
# l3.extend([8,9,10])
# print(l3, l1)
# # Second copy option
# l4 = l1[:]
# l4.extend(['+', '+', '+'])
# print(l4, l1)

# Reverse list
# print("\n----Reverse----")
# # Option 1 list().reverse()
# l = [1,2,3,4,5,6]
# lr = l.reverse()
# print(l, lr)
# print("\n")
# # Option 2 reversed(list())
# l = [1,2,3,4,5,6]
# lr = reversed(l)
# print(l, lr)
# print(l, list(lr))


