# Given an array of positive and negative numbers, arrange them in an alternate fashion such that every 
# positive number is followed by negative and vice-versa maintaining the order of appearance. 
# Number of positive and negative numbers need not be equal. If there are more positive numbers
# they appear at the end of the array. If there are more negative numbers, they too appear in the end of the array.

# Examples : 

# Input:  arr[] = {1, 2, 3, -4, -1, 4}
# Output: arr[] = {-4, 1, -1, 2, 3, 4}

# Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
# output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}


def rearrange(array):
	n = len(array)
	i = 0
	while i < n:
		if array[i] >= 0:
			for j in range(i+1, n):
				if array[j] < 0:
					array[i+1], array[j] = array[j], array[i+1]
			if j == n:
				break
		else:
			for j in range(i+1, n):
				if array[j] >= 0:
					array[i+1], array[j] = array[j], array[i+1]
			if j == n:
				break
		i += 2

def mergesort(array):
	if len(array)>1:
		mid = len(array)//2
		left = array[:mid]
		right = array[mid:]

		mergesort(left)
		mergesort(right)

		i = 0
		j = 0
		k = 0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				array[k] = left[i]
				i += 1
				k += 1
			else:
				array[k] = right[j]
				j += 1
				k += 1

		while i < len(left):
			array[k] = left[i]
			i += 1
			k += 1

		while j < len(right):
			array[k] = right[j]
			j += 1
			k += 1

def reaarange_eff(array):
	mergesort(array)
	n = len(array)
	i = 0
	n_count = 0
	for i in range(n):
		if array[i] < 0:
			n_count += 1
	n_index = 0
	p_index = n_count
	while n_index+1 != p_index:
		array[n_index+1], array[p_index] = array[p_index], array[n_index+1]
		n_index += 2

A = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]


reaarange_eff(A)
print(A)