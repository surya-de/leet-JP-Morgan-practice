from collections import deque
class Solution:
	def numIslands(self, grid):
		ctr = 0
		# This module will initiate the
		# BFS traversal.
		for row in range(0, len(grid)):
			for col in range(0, len(grid[0])):
				# Initiate BFS if the value
				# is 1.
				if grid[row][col] == '1':
					# Update the value in matrix
					grid[row][col] = '0'
					self.traverse_bfs(grid, row, col)
					# Increment counter
					ctr += 1
		return ctr
	# This module will traverse
	# the grapf using BFS.
	def traverse_bfs(self, grid, r, c):
		que = deque()
		# From each coordinate the trversal can
		# be performed in 4 possible directions.
		possible_positions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
		# Append the coordinate in the BFS queue.
		que.append((r, c))
		# Iterate for all the values in Queue.
		while que:
			# Get the traversed coordinate.
			(a, b) = que.popleft()
			# Iterate through all the possible
			# positions for traversed coordinate.
			for position in possible_positions:
				# Check if the position is valid
				# and if the value at position is
				# '1'.
				if (self.validity_check(grid, a + position[0], b + position[1])
					and grid[a + position[0]][b + position[1]] == '1'):
					grid[a + position[0]][b + position[1]] = '0'
					# Append the coordinate in BFS queue.
					que.append((a + position[0], b + position[1]))
	# This module checks the validity of
	# the position to be traversed.
	def validity_check(self, grid, c_row, c_col):
		# The valid position muct have a row and
		# column value greater or equal to 0 and
		# must be less the the length.
		if (c_row >= 0 and c_row < len(grid)
			and c_col >= 0 and c_col < len(grid[0])):
			return True
		# Else
		return False
# The Driver module
if __name__ == '__main__':
	ls = [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]
	s = Solution()
	s.numIslands(ls)



