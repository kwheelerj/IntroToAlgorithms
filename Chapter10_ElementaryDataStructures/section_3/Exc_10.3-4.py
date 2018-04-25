__author__ = 'kwheelerj'

# It is often desirable to keep all elements of a doubly inked list compact in storage,
# using, for example, the first m index locations in the multiple-array representation.
# (This is the case in a paged, virtual-memory computing environment.)  Explain how to
# implement the procedures ALLOCATE-OBJECT and 	FREE-OBJECT so that the representation
# is compact.  Assume that there are no pointers to elements of the linked list outside
# the list itself.  (Hint: Use the array implementation of a stack.)

# Note: implementation in Exc_10.3-2 is compact, but has "pointer" index outside of list itself.


class Memory:

	def __init__(self, length):
		self.length = length
		self.data = [None] * length
		self.free = []
		for i in range(length):
			self.free.append(length-1-i)

	def allocate_object(self, length):
		if len(self.free) is 0:
			print("Error: out of space")
			return -1
		index = self.free.pop()
		for i in range(length-1):
			self.free.pop()
		return index

	def free_object(self, x, length):
		for i in range(length):
			self.free.append(x+(length-1-i))


class DoublyLinkedList(Memory):

	def __init__(self, length=5):
		super().__init__(length)
		self.head = -1
		self.data_length = 3
		self.key_offset = 0
		self.next_offset = 1
		self.prev_offset = 2

	def insert(self, value):
		free_index = super().allocate_object(self.data_length)
		print("free index = {}".format(free_index))
		if free_index is -1:
			return
		self.data[free_index+self.key_offset] = value
		if self.head is -1:
			self.data[free_index+self.prev_offset] = -1
			self.data[free_index+self.next_offset] = -1
		else:
			self.data[free_index+self.next_offset] = self.head
			self.data[free_index+self.prev_offset] = -1
			self.data[self.head+self.prev_offset] = free_index
		self.head = free_index

	def delete(self, x):
		index = self.search(x)
		if index is -1:
			return
		if index is self.head:
			new_head = self.data[index+self.next_offset]
			self.data[new_head + self.prev_offset] = -1
			self.head = new_head
			self.data[index] = index + self.next_offset
		else:
			prev_index = self.data[index+self.prev_offset]
			self.data[prev_index + self.next_offset] = self.data[index+self.next_offset]
			next_index = self.data[index+self.next_offset]
			self.data[next_index + self.prev_offset] = self.data[index+self.prev_offset]

		self.free_object(index, self.data_length)

	def search(self, x):
		i = 0
		while i < self.length:
			if self.data[i] is x:
				return i
			i += self.data_length
		print("'{}' was not found.".format(x))
		return -1

	def disp(self):
		print('*' * 50)
		print('free = [ ', end='')
		for i in range(len(self.free)):
			print('{}'.format(self.free[len(self.free)-1-i]), end=', ')
		print(']')
		print('head = {}'.format(self.head))
		for i in range(self.length):
			if (i + self.data_length) % 3 == 0:
				print('| ', end='')
			print(self.data[i], end=' ')
		print('|')
		print('*' * 50)
		self.print_order()

	def print_order(self):
		index = self.head
		while index != -1:
			print(self.data[index], end=', ')
			index = self.data[index+self.next_offset]
		print()
		print('*' * 50)


if __name__ == '__main__':
	d = DoublyLinkedList(3 * 5)
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
