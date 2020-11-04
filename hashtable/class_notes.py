class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        #self.bucket_array = [None] * capacity
        #self.capacity = capacity
        #self.item_count = 0
        self.capacity = max(capacity, MIN_CAPACITY)
        self.storage = [None] * self.capacity
        self.load = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.storage)
        


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.item_count / self.get_num_slots()


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        XOR operator is exclusive or

        ex.)

        1010
        1100
        ----
        0111

        - start hash at some large number (FNV_offset_basis)
        - the hashed variable maintains our total

        -hashing functions are used in....
        git
        cryptocurrencies
        hash tables
        storing passwords

        -choose between hashing function
        some are fast, some are slow

        -whats reversing a hash mean?
        take a hash number and try to get back to the string it was made from

        ex.) say passwords are hashed
        -p@$$w0rd
        -12324294859x34059efc

        -by nature hash functions are....
        deterministic
        irreversible

        -what are some different strategies to handle collisions?
        chaining: array of linked lists with one LL per index, each node.next point to the second element
        an array of arrays or sub arrays, one array per index
        disallow collisions?
        Python now uses - Open addressing
            - Open addressing, aka, linear probing, quadratic probing, [None, 'hello', 'world', None]

        """
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211
        hashed = FNV_offset_basis

        bytes_to_hash = key.encode()

        for byte in bytes_to_hash:
            hashed = hashed * FNV_prime

            hashed = hashed ^ byte

        return hashed

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        why 5381 and * 33? they just work! nobody knows why...

        What's work? what makes these good?
        - irreversible
        - distributed evenly throughout a modulo operation
        - (which spreads them out over an array & minimizes collisions)
        """
        hashed = 5381

        bytes_to_hash = key.encode()

        for byte in bytes_to_hash:
            # the '<<' shifts the bytes to the left by 5
            hashed = ((hashed << 5) + byte)
            # hashed = ((hashed * 33) + byte)
        
        return hashed


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.get_num_slots()

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # hash the key - self.hash_index will modulo it
        idx = self.hash_index(key)

        # insert the value at that location
        self.storage[idx] = value

        # adding to counter in init
        self.load += 1


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # hash the jey to find the index
        idx = self.hash_index(key)

        #check for collision
        if self.storage[idx] != None:
            print('Warning! Collision!!!')

        if self.storage[idx] == None:
            print('Warning! No key!!!')
        
        else:
            self.storage[idx] = None

            # subtracting from counter in init
            self.load -= 1


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        key_hash = self.djb2(key)
        storage_index = key_hash % self.get_num_slots()

        existing_node = self.storage[storage_index]
        
        if existing_node:
            while existing_node:
                if existing_node == key:
                    return existing_node.value
                existing_node = existing_node.next

        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
