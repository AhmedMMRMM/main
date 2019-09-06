class Iterator:
	def __init__(self,sequence):
		self.seq = sequence
		self.k = -1
		print(self.seq)
	def __getitem__(self,i):
		return self.seq[i]
	def __setitem__(self,j,val):
		self.seq[j] = val
	def __next__(self):
		self.k += 1
		if self.k > len(self.seq):
			k = -1
			#raise StopIteration
		self.k +=1
		return self.seq[self.k]
	def __iter__(self):
		return self
