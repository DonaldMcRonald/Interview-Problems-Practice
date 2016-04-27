"""
Write a function to flatten a nested list. For example,
flatten([1, [2, 3], [4, [5, 6, 7], 8], 9, 0]) => [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
"""

def flatten(arr):
	response = []

	for elem in arr:
		if isinstance(elem, list):
			response.extend(flatten(elem))
		else:
			response.append(elem)

	return response

print flatten([1,[2,3],[4,[5,6,7],8],9,0])
