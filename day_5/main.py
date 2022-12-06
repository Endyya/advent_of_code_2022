import re

class Crate():
	def __init__(self, content):
		self.content = content
	
class Stack():
	def __init__(self, ID):
		self.ID = ID
		self.crates = []

	def __repr__(self):
		return str([crate.content for crate in self.crates])

	def add_crate(self, crate):
		self.crates.append(crate)

	def add_crates(self, crates):
		for crate in crates:
			self.add_crate(crate)

	def move_top_crate(self, stack):
		crate = self.crates.pop()
		stack.add_crate(crate)

	def move_crates(self, number, stack):

		crates = self.crates[-number:]

		self.crates = self.crates[:-number]

		stack.add_crates(crates)

	def get_top(self):
		return self.crates[-1]

class CargoCrane():

	def __init__(self, ID):
		self.ID = ID
		self.stacks = []

	def __repr__(self):
		representation = ''
		for stack in self.stacks:
			representation += stack.__repr__() +'\n'
		return representation

	def add_stack(self, ID):
		new_stack = Stack(ID = ID)
		self.stacks.append(new_stack)

	def get_stack(self, ID):
		return [stack for stack in self.stacks if stack.ID == ID].pop()

	def execute_order(self, line, part = 1):

		orderRegex = re.compile(r'move ([0-9]+) from ([0-9]+) to ([0-9]+)')
		move, origin, target = orderRegex.match(line).group(1, 2, 3)
		stack_origin = self.get_stack(int(origin))
		stack_target = self.get_stack(int(target))

		if part == 1:
			for _ in range(int(move)):
				stack_origin.move_top_crate(stack_target)
		elif part == 2:
			stack_origin.move_crates(number = int(move), stack = stack_target)
			
	

def initialize(filename, part = 1):
	f = open(filename, 'r')
	line = f.readline()
	bay = []
	while line != '\n':
		bay.append(line.replace('\n', ''))
		line = f.readline()
		dock = CargoCrane(ID = 0)
	parse_stack_ID = [int(i) for i in bay.pop().split(' ') if i != '']
	for ID in parse_stack_ID:
		dock.add_stack(ID = ID)
	for layer in bay[::-1]:
		crates = [layer[4*i:4*i+4:].replace(' ', '') for i in range(len(layer)//4 + 1)]
		crates = [item.replace('[', '').replace(']', '') for item in crates]
		for item, ID in zip(crates, parse_stack_ID):
			if item != '':
				crate = Crate(item)
				dock.get_stack(ID).add_crate(crate)


	return dock, f

def process(dock, f, part = 1):
	for line in f:
		dock.execute_order(line, part = part)

	return dock

def main(part = 1, test = False):
	if test:
		filename = 'inputtest'
	else:
		filename = 'input'

	dock, f = initialize(filename)

	process(dock, f, part = part)

	message = ''
	for stack in dock.stacks:
		message += stack.get_top().content

	print('The crates at the top of each stacks are : ', message)

if __name__ == '__main__':
	
	#part 1
	main(part = 1)

	#part 2
	main(part = 2)