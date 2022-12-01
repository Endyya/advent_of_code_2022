import bisect as bs
if __name__ == '__main__':
	tmp = 0
	number_top = 3
	sorted_top = [0] * number_top
	maxi_1, maxi_2, maxi_3 = 0, 0, 0
	with open('input') as f:
		for line in f:
			if line in ['\n', '']:
				bs.insort(sorted_top, tmp)
				sorted_top = sorted_top[1:]
				tmp = 0
			else:
				tmp += int(line)
	print(f'The elf carrying the most calories got {sorted_top[-1]} calories')
	print('The top three elves carrying the most calories got :',
			sum(sorted_top), 'calories')
