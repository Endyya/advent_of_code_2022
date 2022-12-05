import string


def get_priority(filename, part = 1):

	with open(filename, 'r') as f:
		for k, line in enumerate(f):
			line = line.replace('\n', '')
			assert len(line) % 2 == 0
			part1 = line[:len(line)//2]
			part2 = line[len(line)//2:]

			# part 1
			if part == 1:
				common_letter = set(part1) & set(part2)
				priority = string.ascii_letters.index(common_letter.pop()) + 1
				yield priority
			# part 2
			# first elf of the group
			elif part == 2 and k % 3 == 0:
				sack_list = [set(line)]
			# second elf of the group
			elif part == 2 and k % 3 == 1:
				sack_list.append(set(line))
			# last elf of the group
			elif part == 2 and k % 3 == 2:
				sack_list.append(set(line))
				badge = set.intersection(*sack_list)
				priority = string.ascii_letters.index(badge.pop()) + 1
				yield priority


def main(part = 1, test = False):
	if test:
		filename = 'inputtest'
	else:
		filename = 'input'

	count = 0
	for priority in get_priority(filename, part = part):
		count += priority

	print('The sum of priorities of duplicates item is :', count)
	
if __name__ == '__main__':
	
	#part 1
	main(part = 1)

	#part 2
	main(part = 2)
