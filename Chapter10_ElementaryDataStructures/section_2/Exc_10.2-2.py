# Implement a stack using a singly linked list L. The operations
# PUSH and POP should still take O(1) time.


class Stack:

	def __init__(self):
		self.list = SinglyLinkedList()

	def push(self, node):
		self.list.insert(node)

	def pop(self):
		self.list.get_front()

	def print_stack(self):
		self.list.print_list()


class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


class SinglyLinkedList:

	def __init__(self):
		self.head = None

	def insert(self, node):
		node.next = self.head
		self.head = node

	# Will only use this to get head -> O(1)
	def get_front(self):
		if self.head is None:
			return None
		x = self.head
		self.head = self.head.next
		x.next = None
		return x

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

	stack.pop()
	stack.print_stack()
