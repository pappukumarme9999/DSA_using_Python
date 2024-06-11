class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, key, value):
        new_node = Node(key, value)
        if self.head == None:
            self.head = new_node
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def insert_after(self, after, key, value):
        new_node = Node(key, value)
        current = self.head
        while current != None:
            if current.key == after:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        return 'Data not found'

    def __str__(self):
        if self.head == None:
            return "Empty LinkedList"
        str_result = ""
        current = self.head
        while current:
            str_result += f"{current.key}-->{current.value} -> "
            current = current.next
        return str_result.rstrip(" -> ")

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def remove(self, key):
        if self.head == None:
            raise KeyError("Empty LinkedList")
        if self.head.key == key:
            self.head = self.head.next
            return
        current = self.head
        while current.next != None:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next
        raise KeyError(f"Key not found: {key}")

    def search_by_value(self, key):
        current = self.head
        index = 0
        while current != None:
            if current.key == key:
                return index
            current = current.next
            index += 1
        return -1

    def get_node_at_index(self, index):
        current = self.head
        count = 0
        while current != None:
            if count == index:
                return current
            current = current.next
            count += 1
        return None

    def contains(self, key):
        current = self.head
        while current  != None:
            if current.key == key:
                return True
            current = current.next
        return False


class Dictionary:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = self.create_array(capacity)

    def create_array(self, capacity):
        return [LinkedList() for _ in range(capacity)]

    def get_hash(self, key):
        return abs(hash(key)) % self.capacity

    def get_node_index(self, bucket_index, key):
        return self.buckets[bucket_index].search_by_value(key)

    def rehash(self):
        self.capacity *= 2
        old_buckets = self.buckets
        self.size = 0
        self.buckets = self.create_array(self.capacity)
        for i in old_buckets:
            current = i.head
            while current != None:
                self.insert(current.key, current.value)
                current = current.next

    def insert(self, key, value):
        bucket_index = self.get_hash(key)
        if self.buckets[bucket_index].contains(key) == False:
            self.buckets[bucket_index].append(key, value)
            self.size += 1
            if (self.size / self.capacity) >= 2:
                self.rehash()
        else:
            current = self.buckets[bucket_index].head
            while current != None:
                if current.key == key:
                    current.value = value
                    break
                current = current.next

    def __setitem__(self, key, value):
        self.insert(key, value)

    def get(self, key):
        bucket_index = self.get_hash(key)
        current = self.buckets[bucket_index].head
        while current != None:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(f"Key not found: {key}")

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        bucket_index = self.get_hash(key)
        if self.buckets[bucket_index].contains(key) == True:
            self.buckets[bucket_index].remove(key)
            self.size -= 1
        else:
            raise KeyError(f"Key not found: {key}")

    def __str__(self):
        str_result = "{"
        for bucket in self.buckets:
            current = bucket.head
            while current != None:
                str_result += f"{repr(current.key)}: {repr(current.value)}, "
                current = current.next
        str_result = str_result.rstrip(", ")
        return str_result + "}"

    def __len__(self):
        return self.size


d = Dictionary(10)
d['a'] = 1
d['b'] = 2
d['c'] = 3

print(d) 

print(d['a']) 
print(d['b'])  
print(d['z']) 














































'''

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, key, value):
        if self.head is None:
            self.head = Node(key, value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(key, value)

    def find(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

    def remove(self, key):
        if self.head and self.head.key == key:
            self.head = self.head.next
            return True
        current = self.head
        while current and current.next:
            if current.next.key == key:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(f"{current.key}: {current.value}")
            current = current.next
        return " -> ".join(nodes)

class Dictionary:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [LinkedList() for _ in range(capacity)]

    def get_hash(self, key):
        return abs(hash(key)) % self.capacity

    def rehash(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.size = 0
        self.buckets = [LinkedList() for _ in range(self.capacity)]
        for bucket in old_buckets:
            current = bucket.head
            while current:
                self.insert(current.key, current.value)
                current = current.next

    def insert(self, key, value):
        bucket_index = self.get_hash(key)
        node = self.buckets[bucket_index].find(key)
        if node:
            node.value = value
        else:
            self.buckets[bucket_index].append(key, value)
            self.size += 1
            if self.size / self.capacity >= 0.7:
                self.rehash()

    def __setitem__(self, key, value):
        self.insert(key, value)

    def get(self, key):
        bucket_index = self.get_hash(key)
        node = self.buckets[bucket_index].find(key)
        if node:
            return node.value
        raise KeyError(f"Key not found: {key}")

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        bucket_index = self.get_hash(key)
        if self.buckets[bucket_index].remove(key):
            self.size -= 1
        else:
            raise KeyError(f"Key not found: {key}")

    def __str__(self):
        items = []
        for bucket in self.buckets:
            if bucket.head:
                items.append(str(bucket))
        return "{" + ", ".join(items) + "}"

    def __len__(self):
        return self.size

d = Dictionary(10)
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d) 
print(d['a']) 
print(d['b']) 
del d['a']
print(d) 


'''