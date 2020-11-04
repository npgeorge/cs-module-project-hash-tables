'''
 hash function + array = hash table

 array full of linked lists

 ex.)

 Index      Chain
 0          None
 1          ('foo', 12) --> ('bar', 23) --> ('xyzzy', 99)  # collision happens here.. to fix could just store key at the same time
 2          None
 3          13
 4          None
 5          None

put('foo', 12) # hash to 1
put('baz', 13) # hash to 3
put('bar', 23) # hash to 1

get('bar) --> how do you know which one you want?

How do we do a get??
    how do we determine if its the value we want if we're searching by the key?
    A: store the key unhashed and compare as we iterate/traverse down the linked list

put('bar', 42) # overwrite the 23

put('xyzzy', 99) # hashes to 1 as well!

How do we do a put?
    check if key is linked list, if so overwrite, if not add new Node

How do we do a delete?
Delete('bar')


Linked Lists:
- Singly linked
    has a node.next
- Doubly linked
    has node.next and node.prev

some basic code for both single and doubly linked lists

-simple visualization
Node(next: 23_node, value: 12) ---> Node(next: None, value: 23)

implementing traversal of LL

class SLL:
    def __init__(self):
        self.head = None
    
    def get(self, target_value):
        # start at the head
        node = self.head

        while node is not None:
            # check for the target value
            if node.value == target_value:
                return node
            # check next node
            else:
                node = node.next
    
    def delete(self, target_value):
        # if its a head
        if not self.head:
            return False

        # if LL is empty
        if self.head.value == target_value:
            self.head = self.head.next

        prev_node = self.head
        cur_node = self.head.next

        while cur_node is not None:
            if cur_node.value == target_value:
                prev_node.next = cur_node.next

            else:
                prev_node = cur_node
                cur_node = cur_node.next


--------

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

--------

LOAD FACTOR AND RESIZING


--O(1)--
0 -> A
1 -> B
2 -> C
3 -> D
4 -> E
5 -> F

--O(N)--
0 -> A
1 -> B --> G --> L --> M
2 -> C --> K
3 -> D --> H
4 -> E --> J
5 -> F --> I

Load factor
(number of elements) / (number of slots)

Rule of thumb:
Load factor < 0.7

If load factor < 0.2, hash table is underloaded, so array is bigger than you need

How to resize?
 - How do we resize arrays?
 -- make a new array, double the size of the old one
 -- iterate down the old array, and copy every item over
 -- so it's O(n)

 - for a hash table:
 -- double your backing array
 -- iterate down the old array
 -- and traverse down the linked list
 -- then do a put (aka: hash the key, mod key, put into a node)


---Tooling in General---

Checklist
- Go down checlist
- What took me the longest?
- run, right, fast
- binary seach to debug
- What could I have added in my editor?
- Could I find what I was looking for?
- Can I jump around the codebase really effectively?

Spacemacs
Visual studio code
Vimium plugin using chrome
games to play vim

- keyboard macros, check them out


'''

def put(self, key, value):
    """
    Store the value with the given key.
    Hash collisions should be handled with Linked List Chaining.
    Implement this.
    """
    # hash the key - self.hash_index will modulo it
    idx = self.hash_index(key)

    # insert the value at that location
    value = self.storage[idx]




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
