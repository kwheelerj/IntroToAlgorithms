__author__ = 'kwheelerj'

# Implement the dictionary operations INSERT, DELETE, and SEARCH using singly linked,
# circular lists.  What are the running times of your procedures?


class SinglyLinkedList:

	def __init__(self):
		self.nil = Node(None)
		self.nil.next = self.nil
		self.tail = self.nil

	def insert(self, value):
		node = Node(value)
		node.next = self.nil.next
		self.nil.next = node
		if self.is_empty():
			self.tail = node

	def delete(self, node):
		if node is self.nil:
			return
		current_node = self.nil
		while current_node.next is not node:
			current_node = current_node.next
		current_node.next = node.next
		node.next = None

	def search(self, value):
		current_node = self.nil.next
		while current_node is not self.nil and current_node.key is not value:
			current_node = current_node.next
		return current_node

	def is_empty(self):
		return self.tail is self.nil

	def disp(self):
		x = self.nil.next
		print("[", end='')
		while x is not self.nil:
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

	print(s_list.search(3).key)

