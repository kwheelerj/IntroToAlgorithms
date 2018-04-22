__author__ = 'kwheelerj'

# Show how to implement a queue using two stacks.  Analyze the running time of the queue operations.


class Queue:

	def __init__(self, length):
		self.length = length
		self.enqueue_stack = Stack(length)
		self.dequeue_stack = Stack(length)

	def enqueue(self, value):
		self.transfer_to_enqueue_stack()
		if self.enqueue_stack.push(value):
			return True
		print("Queue Overflow Error")
		return False

	def dequeue(self):
		self.transfer_to_dequeue_stack()
		if self.is_empty():
			print("Queue is empty")
		return self.dequeue_stack.pop()

	def transfer_to_enqueue_stack(self):
		count = 0
		while not self.dequeue_stack.is_empty():
			value = self.dequeue_stack.pop()
			self.enqueue_stack.push(value)
			count += 1
		print('\t\tnumber of ops: {}'.format(count))

	def transfer_to_dequeue_stack(self):
		count = 0
		while not self.enqueue_stack.is_empty():
			value = self.enqueue_stack.pop()
			self.dequeue_stack.push(value)
			count += 1
		print('\t\tnumber of ops: {}'.format(count))

	def is_empty(self):
		return self.dequeue_stack.is_empty()

	def disp(self):
		if self.enqueue_stack.is_empty():
			for i in range(self.length):
				print(self.dequeue_stack.data[self.length - 1 - i], end=', ')
		else:
			for i in range(self.length):
				print(self.enqueue_stack.data[i], end=', ')
		print()
		print('*' * 35)


class Stack:

	def __init__(self, length):
		self.length = length
		self.data = [None] * length
		self.top = -1

	def push(self, x):
		if self.top + 1 == self.length:
			print("\tUnderlying Stack Overflow Error")
			return False
		self.top += 1
		self.data[self.top] = x
		return True

	def pop(self):
		if self.is_empty():
			print("\tUnderlying Stack empty")
			return None
		value = self.data[self.top]
		self.data[self.top] = None
		self.top -= 1
		return value

	def is_empty(self):
		return self.top == -1


if __name__ == '__main__':
	q = Queue(6)
	q.disp()
	q.enqueue(1)
	q.disp()

	q.dequeue()
	q.disp()

	q.enqueue(1)
	q.disp()

	q.enqueue(2)
	q.enqueue(3)
	q.enqueue(4)
	q.enqueue(5)
	q.enqueue(6)
	q.disp()

	q.enqueue(7)
	q.disp()

	q.dequeue()
	q.disp()
	q.dequeue()
	q.dequeue()
	q.dequeue()
	q.dequeue()
	q.dequeue()
	q.disp()

	q.dequeue()
	q.disp()

	q.enqueue(1)
	q.disp()
