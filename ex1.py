# PRIME NUMBERS AND DIVISORS

# Find the number of divisors of n
# O(n) time
def divisors1(n):
	ans = 0
	for i in range(1, n + 1):
		if n % i == 0:
			ans += 1
	return ans


# Find the number of divisors of n
# O(\sqrt{n}) time
def divisors2(n):
	ans = 0
	i = 1
	while i * i <= n:
		if n % i == 0:
			ans += 1
			if i != n / i:
				ans += 1
		i += 1
	return ans


# Find the number of divisors of all numbers in range: [1, n]
# Iterate over multiples rather than potential divisors
# This also gives us all the prime numbers: [1, n]
# O(n * \log{n}) time
def divisors3(n):
	 div = [0] * (n + 1)
	 for i in range(1, n + 1):
	 	# Generate all multiples of i upto n
	 	j = i
	 	while j <= n:
	 		# i is a divisor of j
	 		div[j] += 1
	 		j += i

	 return div


# Find all the prime numbers: [1, n]
# O(n * \log{\log{n}}) time
def sieve_of_eratosthenes(n):
	 prime = [True] * (n + 1)
	 prime[1] = False

	 for i in range(2, n + 1):
	 	if prime[i]:
	 		j = i * i
	 		while j <= n:
	 			prime[j] = False
	 			j += i

	 return prime


def main():
	n = int(input())
	#print(divisors1(n))
	print(sieve_of_eratosthenes(n))


if __name__ == "__main__":
	main()