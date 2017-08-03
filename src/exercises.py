"""
exercises.py

Python exercises and examples.
author: luisalbertogh@hotmail.com
"""

# Math module
import math;

class Exercises:
	# Caculate fibonacci serie.
	# - iter - Number of iterations to calculate
	def fib(self, iter):
		"""
		Calculate fibonacci serie. 0, 1, 1, 2, 3, 5, 8, 13, etc
		"""
		total = 0;
		temp = 0;
		for index in range(0, iter + 1):
			if(index == 1 or index == 2):
				total = 1;
			else:
				total += temp;
			temp = total;

		return total;

	def isPrime(self, num):
		sqrN = int(math.sqrt(num));
		for index in range(sqrN, 0, -1):
			if((num % index) == 0 and index != num and index != 1):
				return False;

		return True;

# Main method
def main():
	exer = Exercises();
	print("Fibonacci for {0} is {1}".format(120, exer.fib(120)));
	print("Number {0} is prime? {1}".format(13, exer.isPrime(13)));

# Invoke main method
if __name__ == "__main__":
	main();