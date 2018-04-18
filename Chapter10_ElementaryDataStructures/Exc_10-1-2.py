__author__ = 'kwheelerj'

# Exercise 10.1-2  Explain how to implement two stacks in one array A[1..n] in
# such a way that neither stack overflows unless the total number of elements
# in both stacks together is n.  The PUSH and POP operations should run in O(1) time.


class DoubleStack:

	def __init__(self, length):
		self.data = [None] * length
		self.top_1 = -1
		self.top_2 = length

	def push_1(self, x):
		if self.top_1 + 1 == self.top_2:
			print("Stack Overflow Error on 1")
		else:
			self.top_1 += 1
			self.data[self.top_1] = x

	def push_2(self, x):
		if self.top_2 - 1 == self.top_1:
			print("Stack Overflow Error on 2")
		else:
			self.top_2 -= 1
			self.data[self.top_2] = x

	def disp(self):
		print('---------------------------')
		print("self.data:")
		for i in self.data:
			print(i, end=', ')
		print()
		print('---------------------------')


if __name__ == '__main__':
	stack = DoubleStack(5)
	stack.disp()
	stack.push_1(4)
	stack.disp()
	stack.push_2(5)
	stack.disp()
	stack.push_2(1)
	stack.disp()
	stack.push_2(2)
	stack.disp()
	stack.push_1(7)
	stack.disp()
	# Should cause stack overflows
	stack.push_1(8)
	stack.disp()
	stack.push_2(9)
	stack.disp()
