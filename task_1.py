class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Initialize the head of the list
        self.head = None

    def reverse(self):
        # Reverse the linked list in place
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self):
        # Sort the linked list using insertion sort
        if self.head is None or self.head.next is None:
            return
        
        sorted_list = None
        current = self.head
        
        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node
        
        self.head = sorted_list

    def sorted_insert(self, sorted_list: Node, new_node: Node) -> Node:
        # Insert a new node into the sorted linked list
        if sorted_list is None or sorted_list.data >= new_node.data:
            new_node.next = sorted_list
            return new_node
        
        current = sorted_list
        while current.next and current.next.data < new_node.data:
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        return sorted_list

    def insert_at_beginning(self, data):
        # Insert a new node at the beginning of the list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        # Insert a new node at the end of the list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        # Insert a new node after the given previous node
        if prev_node is None:
            print("Previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        # Delete the first node with the given key (data)
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        # Search for an element by its data
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        # Print all elements of the list
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def merge_sorted_lists(self, other: 'LinkedList') -> 'LinkedList':
        # Merge two sorted linked lists into one sorted linked list
        merged_list = LinkedList()
        current1 = self.head
        current2 = other.head
        
        while current1 and current2:
            if current1.data <= current2.data:
                merged_list.insert_at_end(current1.data)
                current1 = current1.next
            else:
                merged_list.insert_at_end(current2.data)
                current2 = current2.next
        
        while current1:
            merged_list.insert_at_end(current1.data)
            current1 = current1.next
        
        while current2:
            merged_list.insert_at_end(current2.data)
            current2 = current2.next
        
        return merged_list

# Example usage:

llist = LinkedList()

# Insert nodes at the beginning
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Insert nodes at the end
llist.insert_at_end(20)
llist.insert_at_end(25)

# Print the linked list
print("Linked list:")
llist.print_list()

# Delete a node
llist.delete_node(10)

print("\nLinked list after deleting node with data 10:")
llist.print_list()

# Search for an element in the linked list
print("\nSearching for element 15:")
element = llist.search_element(15)
if element:
    print(element.data)


# Reverse the linked list
llist.reverse()
print("\nReversed linked list:")
llist.print_list()
# Sort the linked list
llist.sort()
print("\nSorted linked list:")
llist.print_list()
# Create another sorted linked list
llist2 = LinkedList()
llist2.insert_at_end(1)
llist2.insert_at_end(3)
llist2.insert_at_end(4)
# Merge the two sorted linked lists
merged_list = llist.merge_sorted_lists(llist2)
print("\nMerged sorted linked list:")
merged_list.print_list()
# The code above implements a singly linked list with various functionalities including insertion, deletion, searching, reversing, sorting, and merging two sorted lists.
