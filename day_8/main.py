import numpy as np


def main(part = 1, test = False):
	if test:
		filename = 'inputtest'
	else:
		filename = 'input'


	with open(filename, 'r') as f:
		forest = [[int(x) for x in line.replace('\n', '')] for line in f.readlines()]

	num_tree = (len(forest) + 2) * (len(forest[0]) + 2)
	base_tree = np.array(forest)
	circle_tree = -np.ones(shape = (base_tree.shape[0] + 2, base_tree.shape[1] +2), dtype = int)
	circle_tree[1:-1, 1:-1] = base_tree
	base_tree = circle_tree + 1
	base_tree = base_tree.reshape(1, *base_tree.shape)

	full = np.repeat(base_tree, repeats = num_tree, axis = 0)
	R = np.repeat(range(base_tree.shape[1]), repeats = base_tree.shape[2]).reshape(base_tree.shape[1:])
	C = np.transpose(R)
	Z = np.repeat(range(num_tree), repeats = num_tree).reshape(full.shape)

	R = np.repeat(R.reshape(base_tree.shape), repeats = num_tree, axis = 0)
	C = np.repeat(C.reshape(base_tree.shape), repeats = num_tree, axis = 0)



	mask_west = np.logical_and(
		Z % base_tree.shape[1] == R,
		Z // base_tree.shape[2] > C)
	mask_east = np.logical_and(
		Z % base_tree.shape[1] == R,
		Z // base_tree.shape[2] < C)
	mask_south = np.logical_and(
		Z % base_tree.shape[1] < R,
		Z // base_tree.shape[2] == C)
	mask_north = np.logical_and(
		Z % base_tree.shape[1] > R,
		Z // base_tree.shape[2] == C)

	mask_position = np.logical_and(
		Z % base_tree.shape[1] == R,
		Z // base_tree.shape[2] == C)


	base_alt = base_tree[0].T
	base_alt = np.repeat(base_alt, repeats = num_tree).reshape(num_tree, *base_tree.shape[1:])
	north_seeing = np.all(np.greater(base_alt, full * mask_north), axis = (1, 2))
	south_seeing = np.all(np.greater(base_alt, full * mask_south), axis = (1, 2))
	east_seeing = np.all(np.greater(base_alt, full * mask_east), axis = (1, 2))
	west_seeing = np.all(np.greater(base_alt, full * mask_west), axis = (1, 2))
	testing = np.logical_or(
		np.logical_or(
			south_seeing,
			north_seeing),
		np.logical_or(
			east_seeing,
			west_seeing))

	print(sum(testing))
	check = 15
	#print(base_alt[check])
	#print(full[check])
	#print(testing[check])
	#print((full * mask_north)[check])
	#print(np.greater(base_alt, full * mask_north)[check])




if __name__ == '__main__':
	
	#part 1
	main(part = 1, test = False)

	#part 2
	#main(part = 2, test = True)