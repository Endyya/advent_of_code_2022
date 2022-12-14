class ClockCircuit():
	def __init__(self):
		self.cycle = 1
		self.X = 1
		self.pending = ''
		self.CRT = ''
		self.screen = ''
		self.sprite = '###                                     '

	def reset_CRT(self):
		self.CRT = ''

	def cycles(self, f):
		line = 'init'
		while line != '':
			if self.cycle % 40 == 1:
				self.screen += self.CRT + '\n'
				self.CRT = ''

			self.CRT += self.sprite[(self.cycle - 1) % 40]
			if self.pending == '':
				line = f.readline()
				if line.startswith('addx'):
					value = int(line.split(' ')[-1])
					self.pending = 'addx'
			elif self.pending == 'addx':
				self.pending = ''
				self.X += value
				self.sprite = ' ' * (self.X - 1) + '#' * 3 + ' ' * (40 - self.X - 2)

			else:
				raise Exception

			yield self.cycle
			self.cycle += 1
			

	def get_signal_strength(self):
		return self.cycle * self.X



def main(part = 1, test = False):
	if test:
		filename = 'inputtest'
	else:
		filename = 'input'

	count = 0
	clock = ClockCircuit()
	with open(filename, 'r') as f:
		for cycle in clock.cycles(f):
			if cycle % 40 == 20 and cycle < 230:
				count += clock.get_signal_strength()



	if part == 1:
		print(f'The cumulated signal strenght is : {count}')
	elif part == 2:
		print(clock.screen)

		
if __name__ == '__main__':
	
	#part 1
	main(part = 1, test = False)

	#part 2
	main(part = 2, test = False)
