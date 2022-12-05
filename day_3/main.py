import string


def get_priority(filename):

	with open(filename, 'r') as f:
		for line in f:
			line = line.replace('\n', '')
			assert len(line) % 2 == 0
			part1 = line[:len(line)//2]
			part2 = line[len(line)//2:]

			common_letter = set(part1) & set(part2)
			priority = string.ascii_letters.index(list(common_letter)[0]) + 1

			yield priority

if __name__ == '__main__':
	
	#part 1
	count = 0
	for priority in get_priority('input'):
		count += priority

	print('The sum of priorities of duplicates item is :', count)