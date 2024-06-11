class Dictionary:
    def __init__(self, size):
        self.size = size
        self.slots = [None]*self.size
        self.data = [None]*self.size

    # only immutable datatypes can be hashed 
    def hash_function(self, key):
        return abs(hash(key))%self.size

    # linear probing -> open addressing
    def rehash(self, old_hash_value_position):
        return (old_hash_value_position + 1) % self.size

    def put(self, key,  value):
        hash_value_position = self.hash_function(key)

        if self.slots[hash_value_position] == None:
            self.slots[hash_value_position] = key
            self.data[hash_value_position] = value

        else:
            if self.slots[hash_value_position] == key:
                self.data[hash_value_position] = value
            else:
                new_hash_value_position = self.rehash(hash_value_position)
                
                while (self.slots[new_hash_value_position]!= None) and (self.slots[new_hash_value_position]!= key):
                    new_hash_value_position = self.rehash(new_hash_value_position)
                    if new_hash_value_position == hash_value_position:
                        raise Exception("Hash table is full")
                
                if self.slots[new_hash_value_position] == None:
                    self.slots[new_hash_value_position] = key
                    self.data[new_hash_value_position] = value
                else:
                    self.data[new_hash_value_position] = value


    def get(self, key):
        start_position = self.hash_function(key)
        current_position = start_position
        while current_position != None:
            if self.slots[current_position] == key:
                return self.data[current_position]
            else:
                current_position = self.rehash(current_position)
                if current_position == start_position:
                    return "Dict Traversed(Head to Head) \n Data Not Found"     #when the  dictionary is full and the key is not found
        return "None Found \nData Not Found"     
    

    def  __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
            return self.get(key)
    
    def __str__(self):
        items = []
        for i in range(self.size):
            if self.slots[i]!= None:
                items.append(f"{repr(self.slots[i])}: {repr(self.data[i])}")
        return "{" + ", ".join(items) + "}"


hd = Dictionary(6)

print(hd.slots)
print(hd.data)
print()

print("setting items".center(50,'-'))

hd.put('a', 1)
# print(hd.hash_function('a'))
# print(hd.slots)
# print(hd.data)

print('----------------------------------------')

hd.put('b', 2)
# hd.put('c', 300)
# print(hd.slots)
# print(hd.data)

# print('----------------------------------------')

hd['code1'] = 52130
hd['code2'] = 354541
hd[9999] = '52130'
# print(hd.slots)
# print(hd.data)

# print('----------------------------------------')

# print("value of code1 = ",hd.get('code1'))
# print("value of c = ", hd['c'])

# print('----------------------------------------')

# print("value of tea :\n", hd['tea'])
# print('----------------------------------------')

print(hd)
