class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class DoublyLinkedListNode(LinkedListNode):
    def __init__(self, val):
        LinkedListNode.__init__(self, val)
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_front(self, val):
        new_node = LinkedListNode(val)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def add_back(self, val):
        new_node = LinkedListNode(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_front(self):
        if self.head is None or self.head is self.tail:
            val = self.head.val if self.head else None
            self.head = self.tail = None
            return val

        val = self.head.val
        self.head = self.head.next
        return val

    def remove_back(self):
        if self.head is None or self.head is self.tail:
            val = self.head.val if self.head else None
            self.head = self.tail = None
            return val

        cursor = self.head
        while cursor.next.next:
            cursor = cursor.next
        val = cursor.next.val
        self.tail = cursor
        self.tail.next = None
        return val

class DoublyLinkedList(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)

    def add_front(self, val):
        new_node = DoublyLinkedListNode(val)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def add_back(self, val):
        new_node = DoublyLinkedListNode(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove_front(self):
        if self.head is None or self.head is self.tail:
            val = self.head.val if self.head else None
            self.head = self.tail = None
            return val

        val = self.head.val
        self.head.next.prev = None
        self.head = self.head.next
        return val