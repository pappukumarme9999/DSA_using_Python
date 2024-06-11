class Dictionary:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key):
        return abs(hash(key)) % self.size

    # quadratic probing -> open addressing
    def rehash(self, old_hash_value_position, i):
        return (old_hash_value_position + i**2) % self.size

    def put(self, key, value):
        hash_value_position = self.hash_function(key)

        if self.slots[hash_value_position] is None:
            self.slots[hash_value_position] = key
            self.data[hash_value_position] = value
        else:
            if self.slots[hash_value_position] == key:
                self.data[hash_value_position] = value
            else:
                i = 1
                new_hash_value_position = self.rehash(hash_value_position, i)
                while (self.slots[new_hash_value_position] is not None and
                       self.slots[new_hash_value_position] != key):
                    i += 1
                    new_hash_value_position = self.rehash(hash_value_position, i)
                    if new_hash_value_position == hash_value_position:
                        raise Exception("Hash table is full")

                if self.slots[new_hash_value_position] is None:
                    self.slots[new_hash_value_position] = key
                    self.data[new_hash_value_position] = value
                else:
                    self.data[new_hash_value_position] = value

    def get(self, key):
        start_position = self.hash_function(key)
        current_position = start_position
        i = 1
        while self.slots[current_position] is not None:
            if self.slots[current_position] == key:
                return self.data[current_position]
            current_position = self.rehash(start_position, i)
            i += 1
            if current_position == start_position:
                return "Dict Traversed (Head to Head) \n Data Not Found"
        return "None Found \nData Not Found"

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)
    
    def __str__(self):
        items = []
        for i in range(self.size):
            if self.slots[i] is not None:
                items.append(f"{repr(self.slots[i])}: {repr(self.data[i])}")
        return "{" + ", ".join(items) + "}"
    
