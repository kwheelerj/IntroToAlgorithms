__author__ = 'kwheelerj'

# The dynamic-set operation UNION takes two disjoint sets S1 and S2 as input,
# and it returns a set S = S1 U S2 consisting of all the elements of S1 and S2.
# The sets S1 and S2 are usually destroyed by the operation.  Show how to support
# UNION in O(1) time using a suitable list data structure.


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


class Node:

	def __init__(self, value):
		self.key = value
		self.next = None


if __name__ == '__main__':
	s_list = SinglyLinkedList()
	s_list.insert(1)
	s_list.insert(2)
	s_list.disp()

	s_list.insert(3)
	s_list.disp()

	del_node = s_list.search(3)
	s_list.delete(del_node)
	s_list.disp()

	print(s_list.search(3))

	s_list.insert(3)

	s_list2 = SinglyLinkedList()
	s_list2.insert(9)
	s_list2.insert(8)
	s_list2.insert(7)

	s_list.disp()
	s_list2.disp()

	s_list.union(s_list2)
	
	s_list.disp()
	s_list2.disp()
