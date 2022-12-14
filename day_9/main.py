def update(pos_head, pos_tail):
	# update the tail

	rel_pos = (0, 0)
	if pos_head[0] == pos_tail[0] + 2:
		rel_pos = (
			rel_pos[0] - 1,
			rel_pos[1] + 0)
	if pos_head[0] == pos_tail[0] - 2:
		rel_pos = rel_pos = (
			rel_pos[0] + 1,
			rel_pos[1] + 0)
	if pos_head[1] == pos_tail[1] + 2:
		rel_pos = (
			rel_pos[0] - 0,
			rel_pos[1] - 1)
	if pos_head[1] == pos_tail[1] - 2:
		rel_pos = (
			rel_pos[0] - 0,
			rel_pos[1] + 1)
	if max(
		abs(pos_head[0] - pos_tail[0]),
		abs(pos_head[1] - pos_tail[1])) < 2:

		rel_pos = (
			pos_tail[0] - pos_head[0],
			pos_tail[1] - pos_head[1])

	pos_tail = (
		pos_head[0] + rel_pos[0],
		pos_head[1] + rel_pos[1]
		)
	return pos_tail

def move(direction, pos_head):

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

	return new_pos_head

def main(part = 1, test = False):
	if test and part == 1:
		filename = 'inputtest'
	elif test and part == 2:
		filename = 'inputtestp2'
	else:
		filename = 'input'

	if part == 1:
		rope_size = 2
	elif part == 2:
		rope_size = 10
	else:
		raise Exception

	pos_knots = [(0, 0)] * rope_size

	history_tail = set([pos_knots[-1]])

	with open(filename, 'r') as f:
		line = f.readline()
		while line != '':

			direction, number = line.split(' ')
			number = int(number)
			for _ in range(number):
				pos_knots[0] = move(direction, pos_knots[0])
				for i in range(rope_size - 1):
					pos_knots[i + 1] = update(pos_knots[i], pos_knots[i + 1])

				history_tail.update([pos_knots[-1]])

			line = f.readline()

	print('The tail of the rope visited', len(history_tail), 'positions')

if __name__ == '__main__':
	
	#part 1
	main(part = 1, test = False)

	#part 2
	main(part = 2, test = False)