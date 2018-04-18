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
	q.disp()
	q.enqueue(1)
	q.disp()
	q.enqueue(3)
	q.enqueue(5)
	q.disp()
	q.dequeue()
	q.disp()
	val = q.dequeue()
	q.disp()
	print(val)
	val = q.dequeue()
	print(val)
	q.disp()
	val = q.dequeue()
	print(val)
	q.disp()
