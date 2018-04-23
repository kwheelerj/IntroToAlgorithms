__author__ = 'kwheelerj'

# Give a O(n)-time nonrecursive procedure that reverses a singly linked list of n elements.
# The procedure should use no more than constant storage beyond that needed for the list itself.


class SinglyLinkedList:

	def __init__(self):
		self.head = None
		self.tail = None

	def insert(self, value):
		node = Node(value)
		node.next = self.head
		self.head = node
		if self.is_empty():
			self.tail = node

	def delete(self, node):
		current_node = self.head
		if current_node is node:
			self.head = node.next
		else:
			while current_node.next is not node:
				current_node = current_node.next
			current_node.next = node.next
		node.next = None

	def search(self, value):
		current_node = self.head
		while current_node is not None and current_node.key is not value:
			current_node = current_node.next
		return current_node

	def union(self, singly_linked_list):
		self.tail.next = singly_linked_list.head
		singly_linked_list.head = None
		self.tail = singly_linked_list.tail
		singly_linked_list.tail = None

	def is_empty(self):
		return self.tail is None

	def disp(self):
		x = self.head
		print("[", end='')
		while x is not None:
			print("{}, ".format(x.key), end='')
			x = x.next
		print("]")
		print("\thead at {}\n\ttail at {}".format(self.head.key, self.tail.key))
		print('\t')
		print("*" * 25)

	def reverse(self):
		node = self.head
		temp = node.next
		while temp is not None:
			next_node = temp
			temp = next_node.next
			next_node.next = node
			node = next_node
		self.head.next = None
		temp = self.tail
		self.tail = self.head
		self.head = temp


class Node:

	def __init__(self, value):
		self.key = value
		self.next = None


if __name__ == '__main__':
	s_list = SinglyLinkedList()
	s_list.insert(5)
	s_list.insert(4)
	s_list.insert(3)
	s_list.insert(2)
	s_list.insert(1)
	s_list.disp()

	s_list.reverse()
	s_list.disp()
