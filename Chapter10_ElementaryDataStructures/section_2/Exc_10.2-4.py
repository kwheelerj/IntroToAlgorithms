__author__ = 'kwheelerj'

# As written, each loop iteration in the LIST-SEARCH' procedure requires two tests:
# one for x != L.nil and one for x.key != k.  Show how to eliminate the test for
# x != L.nil in each iteration.


class DoublyLinkedList:

	def __init__(self):
		self.nil = Node(None)		# sentinel
		self.nil.next = self.nil
		self.nil.prev = self.nil

	def insert(self, value):
		node = Node(value)
		node.next = self.nil.next
		self.nil.next.prev = node
		self.nil.next = node
		node.prev = self.nil

	def is_empty(self):
		return self.nil.next is self.nil

	def delete(self, node):
		node.prev.next = node.next
		node.next.prev = node.prev

	def search(self, value):
		node = self.nil.next
		# while node is not self.nil and node.key is not value:
		while node.key is not None and node.key is not value:
			node = node.next
		return node

	def disp(self):
		print('*' * 50)
		print('[', end='')
		node = self.nil.next
		while node is not self.nil:
			print(node.key, end=', ')
			node = node.next
		print(']')
		print('*' * 50)


class Node:

	def __init__(self, value):
		self.prev = None
		self.key = value
		self.next = None


if __name__ == '__main__':
	d_list = DoublyLinkedList()
	d_list.insert(1)
	d_list.insert(2)
	d_list.disp()

	d_list.insert(3)
	d_list.disp()

	print(d_list.search(3).key)
	print(d_list.search(4).key)
