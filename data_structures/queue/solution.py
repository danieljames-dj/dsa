class Stack:
	def __init__(self):
		self.array = []

	def push(self, value):
		self.array.append(value)

	def pop(self):
		return 'None' if len(self.array) == 0 else self.array.pop()

	def count(self):
		return len(self.array)
	
class Queue:
	def __init__(self):
		self.first = Stack()
		self.second = Stack()
	
	def push(self, value):
		self.first.push(value)
	
	def pop(self):
		if self.second.count() == 0:
			while self.first.count() > 0:
				self.second.push(self.first.pop())
		return self.second.pop()

q = Queue()
while True:
	operation = int(input('1 - push, 2 - pop, 3 - exit\n'))
	if operation == 1:
		push = int(input())
		q.push(push)
	elif operation == 2:
		print(q.pop())
	else:
		break