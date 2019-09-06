import sys
def r(dimension,number_of_forces):
	result=[0]*dimension
	x = []
	for i in range(number_of_forces):
		x.append(list(map(int,input().split())))
	#ctrl+d
	for i in range(len(result)):
		for u in range(len(x)):
			result[i] += x[u][i]
	return result
