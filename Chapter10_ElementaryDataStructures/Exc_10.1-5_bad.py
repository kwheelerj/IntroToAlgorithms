__author__ = 'kwheelerj'

# Whereas a stack allows insertion and deletion of elements at only one end,
# and a queue allows insertion at one end and deletion at the other end,
# a deque (double-ended queue) allows insertion and deletion at both end.
# Write four O(1)-time procedures to insert elements into and delete elements
# from both ends of a deque implemented by an array.

# FAILED implementation to have dynamically sized deque sides.

class Deque:

	def __init__(self, length):
		self.length = length
		self.data = [None] * length
		self.read_1 = -1
		self.write_1 = -1
		self.read_2 = length
		self.write_2 = length

	def enqueue_1(self, value):
		for i in range(1, self.length):
			if ((self.write_1 + i) % self.length == self.write_2
						or self.data[self.write_1 + i] is not None):
				continue
			else:
				self.data[self.write_1 + i] = value
				if self.read_1 == -1:
					self.read_1 = self.write_1
				return True
		print("Overflow on write 1")
		return False

	def enqueue_2(self, value):
		for i in range(1, self.length):
			if ((self.write_2 - i) % self.length == self.write_1
						or self.data[self.write_2 - i] is not None):
				continue
			else:
				self.data[self.write_2 - i] = value
				if self.read_2 == self.length:
					self.read_2 = self.write_2
				return True
			print("Overflow on write 2")
			return False

	def dequeue_1(self):
		if self.read_1 == self.write_1:
			print("Deque 1 is empty")
		else
			value = self.data[self.read_1]
			self.data[self.read_1] = None
			self.read_1 = (self.read_1 + 1) % self.length
			if self.read_1 == self.write_1:
				self.read_1 = -1
				self.write_1 = -1