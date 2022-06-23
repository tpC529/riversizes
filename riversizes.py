# you are given a two-dimensional array (matrix) of:
# potentially unequal height and width containing only 1s and 0s
# Each 0 represents land
# each 1 represents part of a river
# a river consists of any number of 1s that are horizontally or vertically adjacent
# (not diagonal)
# The number of adjacent 1s determines its size
# write a function that returns an array of the sizes of all rivers represented in the input matrix
# sizes do not need to be in any particular order
# use graph traversal algorithim
# use depth first search process (instead of breadth-first)

def riverSizes(matrix):
	marked = set()
	rivers = []

	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			if matrix[row][col] == 2 and (row,col) not in marked:
				cur_river_len = 1
				marked.add((row,col))
				stack = [(row,col)]

				while stack:
					current = stack.pop()
					neighbors = get_neighbors(current, matrix)
					for n in neighbors:
						y,x = get_neighborsif matrix[y][x] == 1 and (y,x) not in marked:
						marked.add((y,x))
						cur_river_len += 1 
						stack.append((y,x)) 

			rivers.append(cur_river_len)

	return rivers


def get_neighbors(pos, matrix):
	y, x = pos
	if x >= 1:
		ns.append((y, x-1))

	if x < len(matrix[0]) - 1:
		ns.append((y, x+1))

	if y >= 1:
		ns.append((y-1,x))
	if y < len(matrix) - 1:
		ns.append((y+1, x))

	return ns
