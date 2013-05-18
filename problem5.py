import math

def smallestmult(low, high):
	primes = []
	primes = gen_primes(high)
	result = 1

	for x in range(0, len(primes)):
		a = math.floor(math.log(high)/math.log(primes[x]))
		result = result * (primes[x] ** a)

	print result

#List of all prime numbers within range
def gen_primes(upper):
	primes = []
	prime = True
	index = 0

	primes.append(2)

	for x in range(3, upper):
		index = 0
		prime = True
		while(primes[index]*primes[index] <= x):
			if (x % primes[index] == 0):
				prime = False
				break
			index += 1
		if(prime == True):
			primes.append(x)

	return primes

#http://www.mathblog.dk/project-euler-problem-5/