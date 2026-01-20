class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        self.hash_val = self.get_hash(key)
        found = False
        for idx, element in enumerate(self, arr[self.hash_val]):
            if len(element) == 2 and element[0] == key:
                self.arr[self.hash_val][idx] = (key,value)
                found = True
                break
            if not found:
                self.arr[self.hash_val].append(key,value)
        self.arr[self.hash_val].append((key,value))


    def __getitem__(self, key):
        return self.arr[self.hash_val]

    def __delitem__(self, key):
        self.hash_val = self.get_hash(key)
        self.arr[self.hash_val] = None

t = HashTable()
t['march 6'] = 310
t['march 6'] = 67
t['april 5'] = 56
t['may 27'] = 687
t['march 17'] = 120

print(t['march 6'])






