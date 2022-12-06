if __name__ == '__main__':
	with open('input', 'r') as f:
		text = f.readline()

	# part 1
	i = 4
	window = text[:4]
	while len(set(window)) < 4:
		i += 1
		window = text[(i-4):i]

	print(f'The first start-of-packet marker is detected at {i} character')

	# part 1
	i = 14
	window = text[:14]
	while len(set(window)) < 14:
		i += 1
		window = text[(i-14):i]

	print(f'The first start-of-packet marker is detected at {i} character')