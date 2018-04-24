__author__ = 'kwheelerj'

# Write the procedures ALLOCATE-OBJECT and FREE_OBJECT for a homogeneous collection
# of objects implemented by the single-array representation.


class Memory:

	def __init__(self, length):
		pass

	def allocate_object(self):
		pass

	def free_object(self, x):
		pass


class DoublyLinkedList(Memory):

	def __init__(self, length=5):
		pass

	def insert(self, value):
		pass

	def delete(self, x):
		pass

	def search(self, x):
		pass

	def disp(self):
		pass

	def print_order(self):
		pass


if __name__ == '__main__':
	d = DoublyLinkedList()
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
