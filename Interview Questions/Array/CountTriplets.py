import math as mt
def countWays(arr, n):
	max_val = 0
	for i in range(n):
		max_val = max(max_val, arr[i])

	freq = [0 for i in range(max_val + 1)]

	for i in range(n):
		freq[arr[i]] += 1

	ans = 0 # stores the number of ways

	# Case 1: 0, 0, 0
	ans += (freq[0] * (freq[0] - 1) *
		(freq[0] - 2) // 6)

	# Case 2: 0, x, x
	for i in range(1, max_val + 1):
		ans += (freq[0] * freq[i] *
			(freq[i] - 1) // 2)

	# Case 3: x, x, 2*x
	for i in range(1, (max_val + 1) // 2):
		ans += (freq[i] *
			(freq[i] - 1) // 2 * freq[2 * i])

	# Case 4: x, y, x + y
	# iterate through all pairs (x, y)
	for i in range(1, max_val + 1):
		for j in range(i + 1, max_val - i + 1):
			ans += freq[i] * freq[j] * freq[i + j]

	return ans
arr = [ 1, 2, 3, 4, 5]
n = len(arr)
print(countWays(arr, n))
