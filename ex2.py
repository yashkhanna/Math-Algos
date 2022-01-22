# GCD
# If gcd(a, b) == 1 => a & b are coprime

# Eucledian Algorithm to find gcd(a, b) assuming b > a
	# gcd(a, b) = gcd(a, b - a)
	# Thus, gcd(a, b) = gcd(a, b % a) = gcd(b % a, a)
	# O(\log {\max{a, b}})


def gcd(a, b):
	if a == 0:
		return b
	else:
		return gcd(b % a, a)


def main():
	a = int(input())
	b = int(input())
	print(gcd(a, b))


if __name__ == "__main__":
	main()