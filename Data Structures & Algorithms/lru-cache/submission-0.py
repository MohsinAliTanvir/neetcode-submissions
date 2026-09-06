class Node:

    def __init__(self, val: int, key: int):
        self.val = val
        self.key = key

        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity

        # Head = least recently used
        self.lru = None

        # Tail = most recently used
        self.mru = None

        # key -> Node
        self.cache = {}


    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # If it is already MRU, don't move it
        if node != self.mru:

            # CASE 1: node is currently the LRU/head
            if node == self.lru:

                self.lru = node.next
                self.lru.prev = None

            # CASE 2: node is somewhere in the middle
            else:

                node.prev.next = node.next
                node.next.prev = node.prev


            # Put node at the MRU/tail position
            node.prev = self.mru
            node.next = None

            self.mru.next = node
            self.mru = node

        return node.val


    def put(self, key: int, value: int) -> None:

        # ---------------------------------
        # KEY ALREADY EXISTS
        # ---------------------------------
        if key in self.cache:

            node = self.cache[key]

            # Update value
            node.val = value

            # put() also counts as using the key,
            # so move it to MRU
            if node != self.mru:

                if node == self.lru:

                    self.lru = node.next
                    self.lru.prev = None

                else:

                    node.prev.next = node.next
                    node.next.prev = node.prev


                # Move to tail
                node.prev = self.mru
                node.next = None

                self.mru.next = node
                self.mru = node

            return


        # ---------------------------------
        # NEW KEY
        # ---------------------------------

        node = Node(value, key)

        self.cache[key] = node


        # First node
        if self.lru is None:

            self.lru = node
            self.mru = node

        else:

            # Add new node after current MRU
            self.mru.next = node
            node.prev = self.mru

            self.mru = node


        # ---------------------------------
        # TOO MANY NODES
        # ---------------------------------

        if len(self.cache) > self.capacity:

            old_lru = self.lru

            # Move LRU forward
            self.lru = old_lru.next
            self.lru.prev = None

            # Remove old LRU from dictionary
            del self.cache[old_lru.key]
        
