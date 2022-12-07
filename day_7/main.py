class File():
	def __init__(self, name, size, path):
		self.name = name
		self.size = size
		self.path = path

	def get_size(self):
		return self.size

class Directory():
	def __init__(self, name, path):
		self.name = name
		self.path = path
		self.content = []


	def add_file(self, file):
		self.content.append(file)

	def add_directory(self, new_dir):
		self.content.append(new_dir)

	def get_size(self):
		total_size = 0
		for element in self.content:
			total_size += element.get_size()
		return total_size

class FileSystem():
	def __init__(self, total_space = 0):
		self.cur_pos = '/'
		self.dir_list = {'/': Directory('', '/')}
		self.total_space = total_space

	def create_file(self, line):
		size = int(line.split(' ')[0])
		name = line.split(' ')[1]
		path = self.cur_pos + f'{name}'
		new_file = File(name = name, size = size, path = path)
		self.dir_list[self.cur_pos].add_file(new_file)
		return new_file

	def create_dir(self, line):
		name = ''.join(line.split(' ')[1:])
		path = self.cur_pos + f'{name}/'
		new_dir =  Directory(name = name, path = path)
		self.dir_list[path] = new_dir
		self.dir_list[self.cur_pos].add_directory(new_dir)
		return new_dir

	def get_little_size(self, size_limit):
		count = 0
		for directory in self.dir_list.values():
			if directory.get_size() <= size_limit:
				count += directory.get_size()

		return count

	def get_best_directory_deletion_size(self, needed_space):
		good_candidates = []
		for directory in self.dir_list.values():
			if directory.get_size() >= needed_space:
				good_candidates.append(directory.get_size())

		good_candidates.sort()
		return good_candidates[0]

	def parse_info(self, line):
		if line[:3] == 'dir':
			self.create_dir(line)
		else:
			self.create_file(line)

	def cd(self, path):
		if path == '..':
			new_path = '/'.join(self.cur_pos.split('/')[:-2]) + '/'
		elif path[0] == '/':
			new_path = path
		else:
			new_path = self.cur_pos + f'{path}/'

		self.cur_pos = new_path
		
def main(part = 1, test = False):
	if test:
		filename = 'inputtest'
	else:
		filename = 'input'

	fs = FileSystem(total_space = 70000000)

	with open(filename, 'r') as f:
		for line in f:
			line = line.replace('\n', '')
			if line.startswith('$ cd'):
				in_ls = False
				path = line[5:]
				fs.cd(path)
			elif line.startswith('$ ls'):
				in_ls = True
			elif in_ls:
				fs.parse_info(line)
			else:
				raise Exception

	if part == 1:
		print(fs.get_little_size(size_limit = 100000))
	elif part == 2:
		free_space = fs.total_space - fs.dir_list['/'].get_size()
		need_space = 30000000 - free_space
		print(fs.get_best_directory_deletion_size(needed_space = need_space))

if __name__ == '__main__':
	
	#part 1
	main(part = 1)

	#part 2
	main(part = 2)