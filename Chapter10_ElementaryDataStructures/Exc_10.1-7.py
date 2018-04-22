__author__ = 'kwheelerj'

# Show how to implement a stack using two queues.  Analyze the running time of the stack operations.


class Stack:

	def __init__(self, length):
		self.length = length
		self.count = 0
		self.queue_1 = Queue(length)
		self.queue_2 = Queue(length)

	def push(self, value):
		current_queue = self.get_current_queue()
		if current_queue.enqueue(value):
			self.count += 1
			return True
		print("Stack Overflow Error")
		return False

	def get_current_queue(self):
		current_queue = None
		if not self.queue_1.is_empty():
			current_queue = self.queue_1
		elif not self.queue_2.is_empty():
			current_queue = self.queue_2
		else: # both are empty
			current_queue = self.queue_1
		return current_queue

	def get_other_queue(self):
		other_queue = None
		if self.queue_1.is_empty():
			other_queue = self.queue_1
		elif self.queue_2.is_empty():
			other_queue = self.queue_2
		else:
			print("Logic Error in Code")
		return other_queue

	def pop(self):
		if self.is_empty():
			print("Stack is empty")
			return None
		current_queue = self.get_current_queue()
		self.transfer_all_but_one_to_other_queue()
		self.count -= 1
		# current_queue.disp()
		return current_queue.dequeue()

	def transfer_all_but_one_to_other_queue(self):
		current_queue = self.get_current_queue()
		other_queue = self.get_other_queue()
		for i in range(self.count - 1):
			value = current_queue.dequeue()
			# print(value)
			other_queue.enqueue(value)
			# other_queue.disp()
		print('\t\tnumber of operations: {}'.format(self.count - 1))

	def is_empty(self):
		return self.count == 0

	def disp(self):
		current_queue = self.get_current_queue()
		# print(current_queue.length)
		for i in range(current_queue.length):
			# print((current_queue.head + i) % current_queue.length, end=', ')
			print(current_queue.data[(current_queue.head + i) % current_queue.length], end=', ')
		print()
		# current_queue.disp()


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
			return True
		else:
			print("\tQueue Overflow")
			return False

	def dequeue(self):
		if self.head == self.tail:
			print("\tQueue is empty")
			return None
		else:
			value = self.data[self.head]
			self.data[self.head] = None
			self.head = (self.head + 1) % self.length
			return value

	def is_empty(self):
		return self.head == self.tail

	def disp(self):
		print('\t')
		for i in self.data:
			print(i, end=', ')
		print()
		print("\thead at {}\n\ttail at {}".format(self.head, self.tail))
		print('\t')
		print("*" * 25)


if __name__ == '__main__':
	stack = Stack(6)
	stack.push(1)
	stack.push(2)
	stack.push(3)
	stack.disp()

	stack.pop()
	stack.disp()

	stack.push(4)
	stack.push(5)
	stack.push(6)
	stack.disp()

	stack.push(7)
	stack.push(8)
	stack.disp()

	print('=' * 60)

	# stack.queue_1.disp()
	# stack.queue_2.disp()

	print(stack.pop())
	# stack.queue_1.disp()
	# stack.queue_2.disp()
	stack.disp()
