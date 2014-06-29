# n is the number of natural numbers desired
def diff_sqsum(n):
	return squared_sum(n) - sum_squares(n)

# determines the sum of the squares of the first n natural numbers
def sum_squares(n):
	sum_sq = 0

	for x in range(1, n+1):
		sum_sq += x ** 2

	return sum_sq

# determines the square of the sum of the first n natural numbers
def squared_sum(n):
	sq_sum = 0

	for x in range(1, n+1):
		sq_sum += x

	sq_sum = sq_sum ** 2

	return sq_sum