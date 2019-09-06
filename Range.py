class Range:
	def __init__(self,start,end=None,step=1):
		self.start = start
		self.end = end
		self.step = step
		#To avoid SyntaxError: non-default argument follows default argument
		if end == None:
			self.end , self.start = start , 0
	def __len__(self):
		return self.end
	def __getitem__(self,j):
		item = self.step*j + self.start
		#To insure indexing
		if item >= self.end:
			raise IndexError
		return item