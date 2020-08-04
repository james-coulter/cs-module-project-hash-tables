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


class LinkedList:
    def __init__(self):
        self.head = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [LinkedList()] * capacity
        self.count = 0

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
        return self.count / len(self.storage)

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        hval = 0x811c9dc5
        fnvprime = 0x01000193
        fnvsize = 2**64
        for s in key:
            hval = hval ^ ord(s)
            hval = (hval * fnvprime) % fnvsize
        return hval


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        index = self.hash_index(key)

        if self.storage[index].head is None:
            self.storage[index].head = HashTableEntry(key, value)
            self.count += 1
            return
        else:
            curr = self.storage[index].head

            while curr.next:
                if curr.key == key:
                    curr.value = value
                curr = curr.next
            curr.next = HashTableEntry(key, value)
            self.count += 1



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        curr = self.storage[index].head

        if curr.key == key:
            self.storage[index].head = self.storage[index].head.next
            self.count -= 1
            return
        while curr.next:
            prev = curr
            curr = curr.next
            if curr.key == key:
                prev.next = curr.next
                self.count -= 1
                return None
        # if self.buckets[index] is None:
        #     print("Key does not exist")
        # else:
        #     self.buckets[index] = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        curr = self.storage[index].head

        if curr is None:
            return None
        if curr.key == key:
            return curr.value
        while curr.next:
            curr = curr.next
            if curr.key == key:
                return curr.value
        return None
        # return self.buckets[index]

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity = new_capacity
        new_list = [LinkedList()] * new_capacity

        for i in self.storage:
            curr = i.head

            while curr is not None:
                index = self.hash_index(curr.key)

                if new_list[index].head is None:
                    new_list[index].head = HashTableEntry(curr.key, curr.value)
                else:
                    node = HashTableEntry(curr.key, curr.value)

                    node.next = new_list[index].head

                    new_list[index].head = node
                curr = curr.next
        self.storage = new_list



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
