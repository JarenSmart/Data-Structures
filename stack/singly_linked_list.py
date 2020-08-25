

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next  # The next node in the list


class LinkedList:
    def __init__(self):
        self.head = None  # points to the first node in the list
        self.tail = None  # points to the last node in the list
        self.length = 0

    # append / add --> add_to_tail
    def add_to_tail(self, value):
        if not self.tail and not self.head:
            new_tail = Node(value, None)
            self.head = new_tail
            self.tail = new_tail
        else:
            new_tail = Node(value, None)
            old_tail = self.tail
            old_tail.next = new_tail
            self.tail = new_tail
        self.length += 1

    # Remove Head
    def remove_head(self):
        if not self.head:
            return None

        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return current_head.value
        else:
            current_head = self.head
            self.head = current_head.next
            self.length -= 1
            return current_head.value

    # Remove Tail:
    def remove_tail(self):
        if self.head is None and self.tail is None:
            return None

        # Checking if linked list has only one node.
        if self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            return value  # save current value
        current = self.head
        # Once check is finished and determines there
        # is more than one node, move to else
        while current.next != self.tail:
            current = current.next
        value = self.tail.value
        self.tail = current
        return value

    def add_to_head(self, value):
        # Is there a head?
        # if no head / empty list:
        if self.head is None:
            # create the new node with next = None
            new_node = Node(value, None)
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            # if head exists:
            # create the new node
            # new_node.next = self.head
            new_node = Node(value, self.head)
            # set self.head = new_node
            self.head = new_node
            # increment self.length
            self.length += 1

        # if no head / empty list:
            # create the new node
            # set one with next = None
            # set self.head = new node
            # set self.tail = new node

    def remove_at_index(self, index):
        # Remove at index i:
        # 0) Check that length > i. If not, return None
        if index >= self.length:
            return None
        if self.length == 1 and index == 0:
            target = self.head
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return target.value
        # Iterate through the loop i-1 times:
        prev_node = self.head
        for i in range(index - 1):
            # This will get us to prev_node points to the node before the target node
            prev_node = prev_node.next
        target = prev_node.next
        prev_node.next = target.next
        target.next = None
        self.length = self.length - 1
        return target.value
