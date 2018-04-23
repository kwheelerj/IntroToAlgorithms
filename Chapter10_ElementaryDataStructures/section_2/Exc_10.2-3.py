__author__ = 'kwheelerj'

# Implement a queue by a singly linked list L.
# The operations ENQUEUE and DEQUEUE should still take O(1) time.


class Queue:

	def __init__(self):
		self.list = SinglyLinkedList()

	def enqueue(self, value):
		self.list.insert(Node(value))

	def dequeue(self):
		return self.list.get_front()

	def disp(self):
		self.list.disp()


class SinglyLinkedList:

	def __init__(self):
		self.head = None
		self.tail = None

	# Insert will have to APPEND to the tail
	def insert(self, node):
		if self.tail is None:
			self.head = node
			self.tail = node
		elif self.head is self.tail:
			self.head.next = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

	# Will only use this to get last inserted -> O(1)
	def get_front(self):
		if self.head is None:
			return None
		elif self.head is self.tail:
			x = self.head
			self.head = None
			self.tail = None
			x.next = None
			return x
		else:
			x = self.head
			self.head = self.head.next
			x.next = None
			return x

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
	q = Queue()
	q.disp()

	q.enqueue(1)
	q.enqueue(2)
	q.disp()

	q.dequeue()
	q.disp()

	q.dequeue()
	q.disp()

	q.enqueue(3)
	q.disp()
