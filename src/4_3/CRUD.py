# 完成四大基础数据结构
# 1、 list的CRUD
# CREATE
l1 = []
l1.append('1')
l2 = ['2']
l3 = l1 + l2
l3 += '3'
l4 = ['4'] * 2
l1.insert(0, '0')
print(l1)
print(l3)
print(l4)
# RETRIEVE
print(l1[1])
print(l3[0:2])
print(l3.index('1'))
# print(l3.index(4))
# UPDATE
l1[0] = 0
print(l1)
l3[0:3] = '2'
print(l3)
# DELETE
l2.pop()
print(l2)
l1.clear()
print(l1)
# SORT
list1 = [1,3,2,6,5,4]
list1.sort()
print(list1)
list2 = [1,3,2,6,5,4]
list3 = list(sorted(list2))
print(list3)
list1.reverse()
print(list1)
list4 = list(reversed(list3))
print(list4)

# Tuple的CRUD
# Tuple无CUD
# RETRIEVE
tuple1 = (1,3,4,5)
print(tuple1[3])
print(tuple1[0:3])
print(tuple1.index(3))

# Dict的CRUD
# CREATE
dict1 = {}
dict1['a'] = 1
dict2 = {'b':2}
dict1.update(dict2)
dict1.setdefault('d', 4)
print(dict1)
# RETRIEVE
print(dict1['d'])
print(dict1.get('c'))
print(dict1.keys())
print(dict1.values())
print(dict(dict1.items()))
# UPDATE
dict1['a'] = 0
dict1.update({'b':200})
print(dict1)
# DELETE
dict1.pop('a')
print(dict1)
dict1.popitem()
print(dict1)
dict1.clear()
print(dict1)

# Set的CRUD
# CREATE
set1 = {'a'}
set1.add('b')
print(set1)
# RETRIEVE
print('c' in set1)
# UPDATE
set1.update({'c', 'd'})
set2 = set1.union('f')
print(set1)
print(set2)
# DELETE
set1.remove('d')
print(set1)
print(set1.discard('x'))
set1.pop()
print(set1)
set1.clear()
print(set1)