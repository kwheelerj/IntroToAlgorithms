__author__ = 'kwheelerj'

# Write the procedures ALLOCATE-OBJECT and FREE_OBJECT for a homogeneous collection
# of objects implemented by the single-array representation.


class Memory:

	def __init__(self, length):
		self.length = length
		self.data = [None] * length
		for i in range(length-1):
			self.data[i] = i+1
		self.data[length-1] = -1
		self.free = 0

	def allocate_object(self, length):
		if self.free is -1:
			print("Error: out of space")
			return -1
		index = self.free
		self.free = self.data[self.free + (length-1)]
		return index

	def free_object(self, x, length):
		for i in range(length-1):
			self.data[x+i] = x+(i+1)
		self.data[x+(length-1)] = self.free
		self.free = x


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
		print('free = {}'.format(self.free))
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
