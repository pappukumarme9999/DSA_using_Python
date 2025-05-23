# original list will be changed----------------------
print('normal copy----------------------')
ka = [1, 2, 3]
kb=ka
print("ka is kb => ",ka is kb)
print("ka == kb => ",ka == kb)
kb[0] = 5
print(ka)
print(kb)
print('\n')

import copy

# shallow copy- only the reference of the object is copied - only one level deep copying---------------------
print('shallow copy----------------------')
a = [1, 2, 3]
b = a.copy()
b = copy.copy(a)      # it can be done using copy.copy() as well
print("a is b => ",a is b)
print("a == b => ",a == b)
b[0] = 5
print(a)
print(b)
print('\n')

# deep copy- all levels of the object are copied-----------------------
print('deep copy----------------------')
aa = [[1, 2, 3], [4, 5, 6]]
bb = copy.deepcopy(aa)
print("aa is bb => ",aa is bb)
print("aa == bb => ",aa == bb)
bb[0][0] = 500
print(aa)
print(bb)




# | Use Case                  | Why `deepcopy` Helps                              |
# | ------------------------- | ------------------------------------------------- |
# | Nested dictionaries/lists | Prevent shared references                         |
# | ML experiment configs     | Clone base config safely                          |
# | GUI state trees           | Duplicate UI trees without mutation               |
# | Game development          | Clone entire object trees (e.g. game world state) |
