
def move(direction, pos_head, pos_tail):

	# update the head
	if direction == 'U':
		rel_pos = (0, 1)
	elif direction == 'D':
		rel_pos = (0, -1)
	elif direction == 'L':
		rel_pos = (-1, 0)
	elif direction == 'R':
		rel_pos = (1, 0)
	else:
		raise Exception

	new_pos_head = (
		pos_head[0] + rel_pos[0],
		pos_head[1] + rel_pos[1]
		)

	# update the tail
	if new_pos_head[0] == pos_tail[0] + 2:
		rel_pos = (-1, 0)
	elif new_pos_head[0] == pos_tail[0] - 2:
		rel_pos = (1, 0)
	elif new_pos_head[1] == pos_tail[1] + 2:
		rel_pos = (0, -1)
	elif new_pos_head[1] == pos_tail[1] - 2:
		rel_pos = (0, 1)
	else:
		rel_pos = (
			pos_tail[0] - new_pos_head[0],
			pos_tail[1] - new_pos_head[1])

	new_pos_tail = (
		new_pos_head[0] + rel_pos[0],
		new_pos_head[1] + rel_pos[1]
		)

	return (new_pos_head, new_pos_tail)

def main(part = 1, test = False):
	if test:
		filename = 'inputtest'
	else:
		filename = 'input'

	pos_head = (0, 0)
	pos_tail = (0, 0)

	history_tail = set([pos_tail])

	with open(filename, 'r') as f:
		line = f.readline()
		while line != '':

			direction, number = line.split(' ')
			number = int(number)
			for _ in range(number):
				pos_head, pos_tail = move(direction, pos_head, pos_tail)
				history_tail.update([pos_tail])

			line = f.readline()

	print('The tail of the rope visited', len(history_tail), 'positions')

if __name__ == '__main__':
	
	#part 1
	main(part = 1, test = False)

	#part 2
	main(part = 2, test = True)