dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

#loop to automate initiate dict, have other method to convert first letter to number but would like to use dict
# for i in range(1, 27):
#     letter = chr(ord('a') + i - 1)
#     dict[letter] = i
# print(dict)

class HT:
    # INITIATE THE HASHTABLE
    def __init__(self,size = 5):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    # HASHING FUNCTIONS
    def hash(self,key):
        return dict[key[0]] % self.size

    #didnt manage to figure rehashing using key rather than index...
    # def rehash(self,key):
    #     next_letter = chr((ord(key[0]) - ord('a') + 1) % 26 + ord('a'))
    #     return dict[next_letter] % self.size
    
    def rehash(self,index):
        return (index+1) % self.size

    # GET THE DATA USING THE KEY
    def get(self, key):
        index = self.hash(key)

        # IF THE KEY IS FOUND IMMEDIATELY
        if self.keys[index] == key:
            return self.values[index]
        else:
            # GOING THROUGH THE TABLE TO FIND THE KEY
            oghash = index
            index = self.rehash(index)
            while index != oghash:
                if self.keys[index] == key:
                    return self.values[index]
                else:
                    index = self.rehash(index)  
            return None

    def __getitem__(self,key):
        return self.get(key)

    # PUT THE ITEM INTO THE HASH TABLE
    def put(self, key, value):
        index = self.hash(key)
        if self.keys[index] is None or self.keys[index] == key:
            self.keys[index] = key
            self.values[index] = value
            return
        else:
            oghash = index
            index = self.rehash(index)
            while index != oghash:
                if self.keys[index] is None or self.keys[index] == key:
                    self.keys[index] = key
                    self.values[index] = value
                    return
                else:
                    index = self.rehash(index)
            print("The hash table is already full")

    def __setitem__(self,key,value):
        self.put(key,value)
    
    # AS A PRACTICE, MODIFY/ADD A FUNCTION INSIDE THE CLASS THAT DELETES THE VALUE INSIDE THE HASH TABLE
     
    def delete(self, key): 
        index = self.hash(key)

        # If the key is found immediately
        if self.keys[index] == key:
            self.values[index] = 'deleted'
            self.keys[index] = 'deleted'
            return
        else:
            # Going through the table to find the key
            oghash = index
            index = self.rehash(index)
            while self.keys[index] is not None and index != oghash:
                if self.keys[index] == key:
                    self.values[index] = 'deleted'
                    self.keys[index] = 'deleted'
                    return
                else:
                    index = self.rehash(index)
        print("Key not found in the hash table")
    # Clear whole HT
    def clear(self):
        self.keys = [None] * self.size
        self.values = [None] * self.size

# #Task4
# hash = HT()
# hash['name'] = 'Zikri'
# hash['age'] = 20
# hash['gender'] = 'M'
# print(hash['name'])
# print(hash['age'])
# print(hash['gender'])
# print(hash.keys)
# print(hash.values)
# hash['birthdate'] = '4 December'
# print(hash.keys)
# print(hash.values)
# print(hash['birthdate'])
# hash['name'] = 'Hakim'
# print(hash['name'])
# hash.delete('age')
# print(hash.keys)
# print(hash.values)
# print(hash['age'])
# print(hash['birthdate'])