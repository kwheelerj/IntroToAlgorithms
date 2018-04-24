__author__ = 'kwheelerj'

# Write the procedures ALLOCATE-OBJECT and FREE_OBJECT for a homogeneous collection
# of objects implemented by the MULTI-array representation.


class Memory:

	def __init__(self, length):
		self.length = length
		self.data = [None] * length
		for i in range(1, length):
			self.data[i-1] = i
		self.data[length-1] = -1
		self.free = 0

	def allocate_object(self):
		if self.free is -1:
			print("Error: out of space")
			return None
		else:
			x = self.free
			self.free = self.data[self.free]
			return x

	def free_object(self, x):
		self.data[x] = self.free
		self.free = x


class DoublyLinkedList(Memory):

	def __init__(self, length=5):
		super().__init__(length)
		self.head = -1
		self.next = self.data
		self.key = [-5] * length
		self.prev = [-5] * length

	def insert(self, value):
		free_index = super().allocate_object()
		if free_index is None:
			return
		self.key[free_index] = value
		if self.head is not -1:
			self.prev[self.head] = free_index
		self.prev[free_index] = -1
		self.next[free_index] = self.head
		self.head = free_index

	def delete(self, x):
		index = self.search(x)
		if index is -1:
			return
		if self.next[index] is not -1:
			self.prev[self.next[index]] = self.prev[index]
		if self.prev[index] is not -1:
			self.next[self.prev[index]] = self.next[index]
		if self.prev[index] is -1:
			self.head = self.next[index]
		self.prev[index] = -5
		self.key[index] = -5

		self.free_object(index)
		self.next[index] = self.data[index]

	def search(self, x):
		for i in range(self.length):
			if self.key[i] is x:
				return i
		print("'{}' was not found.".format(x))
		return -1

	def disp(self):
		print('*' * 50)
		print("head: {}".format(self.head))
		print("free: {}".format(self.free))
		print("next", end=' ')
		for i in range(self.length):
			print('{0:5d}'.format(self.next[i]), end=', ')
		print()
		print("key ", end=' ')
		for i in range(self.length):
			print('{0:5d}'.format(self.key[i]), end=', ')
		print()
		print("prev", end=' ')
		for i in range(self.length):
			print('{0:5d}'.format(self.prev[i]), end=', ')
		print()
		print('*' * 50)
		self.print_order()
		print('*' * 50)

	def print_order(self):
		index = self.head
		while index is not -1:
			print(self.key[index], end=',')
			index = self.next[index]
		print()


if __name__ == '__main__':
	d = DoublyLinkedList()
	d.disp()
	d.insert(1)
	d.disp()
	d.insert(2)
	d.disp()
	d.insert(3)
	d.disp()
	d.insert(4)
	d.disp()
	d.insert(5)
	d.disp()

	d.insert(6)
	d.disp()

	d.delete(5)
	d.disp()
	d.delete(3)
	d.disp()

	d.insert(7)
	d.disp()

	d.delete(10)
	d.disp()
