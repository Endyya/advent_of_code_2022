def change_line(line):

	# what should I play to win against any key
	win = {
		'A': 'Y',
		'B': 'Z',
		'C': 'X'}

	# what should I play to draw against any key
	draw = {
		'A': 'X',
		'B': 'Y',
		'C': 'Z'}

	# what should I play to lose against any key
	lose = {
		'A': 'Z',
		'B': 'X',
		'C': 'Y'}

	case = {
		'X': lose,
		'Y': draw,
		'Z': win}

	return line[:2] + case[line[-1]][line[0]]


def get_score(line):
	win = ['A Y', 'B Z', 'C X']
	draw = ['A X', 'B Y', 'C Z']

	possible_move = 'XYZ'

	return possible_move.index(line[-1]) + 3 * (line in draw) + 6 * (line in win) + 1 

def get_scores(file_name, part):

	score = 0

	with open(file_name, 'r') as f:
		line = f.readline().replace('\n', '')

		while line != '':
			if part == 2:
				line = change_line(line)
			score += get_score(line)
			yield score
			line = f.readline().replace('\n', '')

if __name__ == '__main__':
	# part 1
	scores = get_scores('input', part = 1)
	score = next(scores)
	for score in scores:
		pass

	print('Your final score for part 1 is :', score)

	# part 2
	scores = get_scores('input', part = 2)
	score = next(scores)
	for score in scores:
		pass

	print('Your final score for part 2 is :', score)