__author__ = 'kwheelerj'

# Whereas a stack allows insertion and deletion of elements at only one end,
# and a queue allows insertion at one end and deletion at the other end,
# a deque (double-ended queue) allows insertion and deletion at both end.
# Write four O(1)-time procedures to insert elements into and delete elements
# from both ends of a deque implemented by an array.

# Version 2: interpretation of deque


class Deque:

	def __init__(self, length):
		self.length = length
		self.data = [None] * length
		self.head = 0
		self.tail = 0

	def enqueue_1(self, value):
		if (self.tail + 1) % self.length != self.head:
			self.data[self.tail] = value
			self.tail = (self.tail + 1) % self.length
		else:
			print("Queue Overflow")

	def dequeue_1(self):
		if self.head == self.tail:
			print("Queue is empty")
		else:
			value = self.data[self.head]
			self.data[self.head] = None
			self.head = (self.head + 1) % self.length
			return value

	def enqueue_2(self, value):
		if (self.head - 1) % self.length != self.tail:
			self.head = (self.head - 1) % self.length
			self.data[self.head] = value
		else:
			print("Queue Overflow")
		
	def dequeue_2(self):
		if self.head == self.tail:
			print("Queue is empty")
		else:
			self.tail -= 1
			value = self.data[self.tail]
			self.data[self.tail] = None
			return value

	def disp(self):
		for i in self.data:
			print(i, end=', ')
		print()
		print("head at {}\ntail at {}".format(self.head, self.tail))
		print("*" * 25)


if __name__ == '__main__':
	d = Deque(12)
	d.enqueue_1(1)
	d.enqueue_1(2)
	d.enqueue_1(3)
	d.enqueue_1(4)
	d.enqueue_1(5)
	d.enqueue_1(6)
	d.disp()

	d.enqueue_2(91)
	d.enqueue_2(92)
	d.enqueue_2(93)
	d.disp()

	d.dequeue_1()
	d.dequeue_1()
	d.disp()

	d.dequeue_2()
	d.disp()

	d.dequeue_2()
	d.disp()

	d.enqueue_2(64)
	d.enqueue_2(65)
	d.disp()

	d.enqueue_2(66)
	d.enqueue_2(67)
	d.disp()

	d.enqueue_2(68)
	d.disp()

	d.enqueue_1(6)
	d.disp()

	d.enqueue_1(7)
	d.disp()

	d.enqueue_2(69)
	d.disp()
