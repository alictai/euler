if __name__ == "__main__":
	x = 1
	y = 2
	next = x + y
	sum = 2
	while (next < 4000000):
		print next
		if (next % 2 == 0):
			sum += next
		x = y
		y = next
		next = x + y
	print sum