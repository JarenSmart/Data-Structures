

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
        if not self.tail:
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
        # if self.length > 0:
        #     if self.length == 1:
        #         self.head = None
        #         self.tail = None
        #     else:
        #         current = self.head
        #         while current.next != self.tail:
        #             current = current.next
        #         current.next = None
        #         self.tail = current
        #     self.length -= 1

        # Start at head and iterate to the next-to-last node
        # Stop when current_node.next == self.tail
        # Save the current_tail value
        # Set self.tail to current_node
        # Set current_node.next to None
        #
        # List of 1 element:
        # Save the current_tail.value
        # Set self.tail to None
        # Set self.head to None
