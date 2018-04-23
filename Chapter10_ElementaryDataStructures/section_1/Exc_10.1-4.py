__author__ = 'kwheelerj'

# Rewrite ENQUEUE and DEQUEUE to detect underflow and overflow of a queue.
# Queue implementation with "circular" array


class Queue(object):

	def __init__(self, length):
		self.length = length
		self.data = [None] * length
		self.head = 0
		self.tail = 0

	def enqueue(self, value):
		if (self.tail + 1) % self.length != self.head:
			self.data[self.tail] = value
			self.tail = (self.tail + 1) % self.length
		else:
			print("Queue Overflow")

	def dequeue(self):
		if self.head == self.tail:
			print("Queue is empty")
		else:
			value = self.data[self.head]
			self.data[self.head] = None
			self.head = (self.head + 1) % self.length
			return value

	def disp(self):
		for i in self.data:
			print(i, end=', ')
		print()
		print("head at {}\ntail at {}".format(self.head, self.tail))
		print("*" * 25)


if __name__ == '__main__':
	q = Queue(12)
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	q.enqueue(4)
	q.enqueue(5)
	q.enqueue(6)
	q.enqueue(7)
	q.enqueue(8)
	q.enqueue(9)
	q.enqueue(10)
	q.disp()
	q.enqueue(11)
	q.disp()
	q.enqueue(12)
	q.disp()
	q.enqueue(13)

	q.dequeue()
	q.dequeue()
	q.dequeue()
	q.disp()

	q.enqueue(12)
	q.enqueue(13)
	q.enqueue(14)
	q.disp()

	q.enqueue(15)
