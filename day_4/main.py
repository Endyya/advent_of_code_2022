def get_overlap(filename, part = 1):
	with open(filename, 'r') as f:
		for line in f:
			assign1, assign2 = line.split(',')
			start1, stop1 = assign1.split('-')
			start2, stop2 = assign2.split('-')
			start1, start2, stop1, stop2 = int(start1), int(start2), int(stop1), int(stop2)
			if part == 1:
				yield (
					(start1 <= start2 and stop1 >= stop2)
					or (start1 >= start2 and stop1 <= stop2))
			elif part == 2:
				yield (
					(start1 <= start2 and stop1 >= start2)
					or (start1 >= start2 and start1 <= stop2))

def main(part = 1, test = False):
	if test:
		filename = 'inputtest'
	else:
		filename = 'input'

	count = 0
	for over in get_overlap(filename, part = part):
		if over:
			count += 1

	if part == 1:
		conclusion = f'There is {count} assignments included in the other pair assignment'
	elif part == 2:
		conclusion = f'There is {count} assignment overlapping with the other pair assignment'

	print(conclusion)

if __name__ == '__main__':
	
	#part 1
	main(part = 1)

	#part 2
	main(part = 2)