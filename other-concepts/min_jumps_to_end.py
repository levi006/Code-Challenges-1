"""
Minimum number of jumps to reach end


Given an array of integers where each element represents the max number of steps
that can be made forward from that element. Write a function to return the minimum
number of jumps to reach the end of the array (starting from the first element).
If an element is 0, then cannot move through that element.

Example:
	Input:		[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
	Output:		3 (1 -> 3 -> 8 -> 9)

http://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/
"""

# from http://www.careercup.com/question?id=24669663
# recursive with memoization
def min_jumps_to_end(arr, i, path):
	n_steps = float('inf')
	m = arr[i]

	# if can reach the last element with one jump
	if i + m >= len(arr) - 1:
		path[i] = 1
		return 1
	# test every possible jump from 1 to max possible value
	else:
		for j in range(i+1, i+m+1):
			if path[j] is None:
				# will assign a value to path[j]
				min_jumps_to_end(arr, j, path)
			if path[j] < n_steps:
				n_steps = path[j]

		# add to recursive value 1 for this jump
		path[i] = n_steps + 1

		return n_steps + 1

def min_jumps_to_end_wrapper(arr):
	n = len(arr)
	path = []*n

	if n == 1:
		return 0

	return min_jumps_to_end(arr, 0, path)

#########################################################################################

# http://www.careercup.com/question?id=24669663
# greedy without memoization
def greedy_min_jumps_to_end(a, i=0, step_count=0):
	best_step = i
	best_possible = i
	n = len(a)

	if i == n-1:
		return 0

	m = a[i]

	if m+i >= n-1:
		return step_count + 1

	for j in range(i+1, min(n-1, i+m+1)):
		s = a[j] + j
		if s > best_possible:
			best_possible = s
			best_step = j

	if best_step == i:
		return float('inf')
	else:
		return greedy_min_jumps_to_end(a, best_step, step_count+1)

#########################################################################################

# dynamic programming from GFG
# build jumps array such that jumps[i] is the minimum number of jumps need to
# reach arr[i] from arr[0]. return jumps[n-1]
def min_num(x, y):
	if x < y:
		return x
	return y

def min_jumps(arr, n):
	jumps = []*n
	i = 0
	j = 0

	if n == 0 or arr[0] == 0:
		return None

	jumps[0] = 0

	# find the minimum number of jumps to reach arr[i] from arr[0]
	# and assign this value to jumps[i]
	for i in range(1, n):
		jumps[i] = float('inf')
		for j in range(i):
			if i <= j + arr[j] and jumps[j] != float('inf'):
				jumps[i] = min_num(jumps[i], jumps[j] + 1)
				break

	return jumps[n-1]

def min_jumps_wrapper(arr):
	n = len(arr)
	return min_jumps(arr, n)

#########################################################################################

# dynamic programming from GFG
# build jumps array such that jumps[i] is the minimum number of jumps need to
# reach arr[n-1] from arr[i]. return jumps[0]

def min_jumps_v2(arr, n):
	jumps = []*n
	minimum = 0

	# min number of jumps to reach last element from last element itself is always 0
	jumps[n-1] = 0

	i = n-2
	j = 0

	# start from second elemnt, move from right to left and construct jumps array
	# where jumps[i] represents min number of jumps to reach arr[m-1] from arr[i]
	while i >= 0:
		# if arr[i] is 0 then arr[n-1] can't be reached from here
		if arr[i] == 0:
			jumps[i] = float('inf')
		# if we can directly reach to the end point from here then jumps[i] is 1
		elif arr[i] >= n - i - 1:
			jumps[i] = 1
		# otherwise, to find out min number of jumps needed to reach arr[n-1],
		# check all the points reachable from here and jumps[] value for those points
		else:
			minimum = float('inf') # initialize min value
			j = i+1
			# check all reachable points and takes the minimum
			while j < n and j <= arr[i] + i:
				if minimum > jumps[j]:
					minimum = jumps[j]
				j += 1
			# handles overflow
			if minimum != float('inf'):
				jumps[i] = minimum + 1
			else:
				jumps[i] = minimum
		i -= 1

	return jumps[0]
