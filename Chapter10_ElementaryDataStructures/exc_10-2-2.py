# Implement a stack using a singly linked list L. The operations
# PUSH and POP should still take O(1) time.


class Node:

	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


class Stack:

	def __init__(self):
		self.list = List()

	def push(self, node):
		self.list.insert(node)

	def pop(self):
		self.list.pop_front()

	def print_stack(self):
		self.list.print_list()


class List:

	def __init__(self):
		self.head = None

	def insert(self, node):
		node.next = self.head
		if self.head is not None:
			self.head.prev = node
		self.head = node
		node.prev = None

	# Will only use this to get head -> O(1)
	def pop_front(self):
		x = self.head
		self.delete(x)

	def delete(self, node):
		if node.prev is not None:
			node.prev.next = node.next
		else:
			self.head = node.next
		if node.next is not None:
			node.next.prev = node.prev

	def print_list(self):
		x = self.head
		print("[", end='')
		while x is not None:
			print("{}, ".format(x.data), end='')
			x = x.next
		print("]")


if __name__ == '__main__':
	stack = Stack()
	stack.print_stack()
	stack.push(Node(4))
	stack.print_stack()
	stack.push(Node(6))
	stack.print_stack()
	stack.pop()
	stack.print_stack()
	stack.pop()
	stack.print_stack()
