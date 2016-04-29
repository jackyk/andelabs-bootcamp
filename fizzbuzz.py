
def fizz_buzz(A):
	if A % 3 == 0 and A % 5 == 0:
		return "FizzBuzz"

	if A % 3 == 0:
		return "Fizz"

	if A % 5 == 0:
		return "Buzz"

	else:
		return A

print fizz_buzz(1)
