class LinkedList:
    def __init__(self):
        self.root = None
    def insertAtBegin(self, val: int):
        if self.root is None:
            self.root = Node(val)
            return True
        temp = Node(val)

        temp.next = self.root
        self.root = temp
        return True
    def insertAtEnd(self, val: int):
        if self.root is None:
            self.root = Node(val)
            return True
        cur = self.root
        while cur.next is not None:
            cur = cur.next
        cur.next =  Node(val)
        return True
    def insertAtIndex(self, val: int, index: int):
        if index < 0:
            return False
        if index == 0:
            self.insertAtBegin(val)
            return True
        elif index == self.size():
            self.insertAtEnd(val)
            return True
        elif index > self.size():
            return False
        cur = self.root
        counter = 0

        while cur.next is not None:
            if counter == index - 1:
                temp = Node(val)
                temp.next = cur.next
                cur.next = temp
                return True
            counter += 1
            cur = cur.next
        return False
    def print_linked_list(self):
        if self.root is None:
            print("Empty Linked List")
            return True
        cur = self.root
        while cur is not None:
            print(cur.val)
            cur = cur.next
        return True
    def remove(self, target: int):
        if self.root is None:
            return False
        if self.root.val == target:
            self.root = self.root.next
            return True
        cur = self.root
        while cur.next is not None:
            if cur.next.val == target:
                cur.next = cur.next.next
                return True
            cur = cur.next
        return False
    def size(self):
        cur = self.root
        counter = 0
        while cur.next is not None:
            counter += 1
            cur = cur.next
        return counter
class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


linked_list = LinkedList()
linked_list.insertAtBegin(2)
linked_list.insertAtBegin(3)
linked_list.insertAtBegin(4)
linked_list.print_linked_list()


print("______________")
linked_list.remove(3)
linked_list.print_linked_list()


print("______________")
print(linked_list.size())
linked_list.print_linked_list()

print("______________")
linked_list.insertAtEnd(2)
linked_list.insertAtEnd(3)
linked_list.print_linked_list()