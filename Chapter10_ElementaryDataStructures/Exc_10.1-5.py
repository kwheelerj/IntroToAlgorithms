__author__ = 'kwheelerj'

# Whereas a stack allows insertion and deletion of elements at only one end,
# and a queue allows insertion at one end and deletion at the other end,
# a deque (double-ended queue) allows insertion and deletion at both end.
# Write four O(1)-time procedures to insert elements into and delete elements
# from both ends of a deque implemented by an array.

# Version 1, an (incorrect, I think) interpretation of description of deque.


class Deque:

	def __init__(self, length):
		self.length = length
		self.data = [None] * length
		self.length_1 = length // 2
		self.length_2 = length // 2
		if length % 2 != 0:
			self.length_2 += 1
		self.head_1 = 0
		self.tail_1 = 0
		self.head_2 = length - 1
		self.tail_2 = length - 1
		print(self.length_1)
		print(self.length_2)

	def enqueue_1(self, value):
		if (self.tail_1 + 1) % self.length_1 != self.head_1:
			self.data[self.tail_1] = value
			self.tail_1 = (self.tail_1 + 1) % self.length_1
		else:
			print("Queue Overflow")

	def dequeue_1(self):
		if self.head_1 == self.tail_1:
			print("Queue is empty")
		else:
			value = self.data[self.head_1]
			self.data[self.head_1] = None
			self.head_1 = (self.head_1 + 1) % self.length_1
			return value

	def enqueue_2(self, value):
		if ((self.tail_2 - 1 - self.length_1) % self.length_2) + self.length_1 != self.head_2:
			self.data[self.tail_2] = value
			self.tail_2 = ((self.tail_2 - 1 - self.length_1) % self.length_2) + self.length_1
		else:
			print("Queue Overflow")
		
	def dequeue_2(self):
		if self.head_2 == self.tail_2:
			print("Queue is empty")
		else:
			value = self.data[self.head_2]
			self.data[self.head_2] = None
			fd = (self.head_2 - 1 - self.length_1)
			print(fd)
			self.head_2 = (fd % self.length_2) + self.length_1
			return value

	def disp(self):
		for i in self.data:
			print(i, end=', ')
		print()
		print("1: head at {}\ntail at {}".format(self.head_1, self.tail_1))
		print("*" * 25)
		print("2: head at {}\ntail at {}".format(self.head_2, self.tail_2))
		print("*" * 25)
		print("*" * 25)


if __name__ == '__main__':
	d = Deque(12)
	d.enqueue_1(1)
	d.enqueue_1(2)
	d.enqueue_1(3)
	d.enqueue_1(4)
	d.enqueue_1(5)
	d.disp()
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
	d.enqueue_1(8)
	d.disp()
