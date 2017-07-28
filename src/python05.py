"""
python05.py

Python classes 05 - Decorators and mixins
author: luisalbertogh@hotmail.com
"""

import math;
import functools;
import logging;
import logging.config;
import sys;
import yaml;

"""
Class with decorators.
"""
class Calculator:
	# Static method
	@staticmethod
	def sum(num1, num2):
		return num1 + num2;

	# Lazy property
	@property
	def pi(self):
	    return math.pi;
	
"""
Class with standard decorators.
"""
# Automatic ordering
@functools.total_ordering
class Warrior:
	def __init__(self, strength, life):
		self.strength = strength;
		self.life = life;

	# Define at least one comparison operator
	def __eq__(self, other):
		return self.strength == other.strength and self.life == other.life;

	def __lt__(self, other):
		return self.strength < other.strength and self.life < other.life;


"""
Main method
"""
def main():
	# Logger
	logdict = yaml.load(open('config/log_config.yaml', 'r'));
	logging.config.dictConfig(logdict);
	#logging.basicConfig(stream=sys.stdout, level=logging.DEBUG);
	logger = logging.getLogger('MyLogger');

	# Static method
	num1, num2 = 2, 2;
	total = Calculator.sum(num1, num2);
	logger.info('{0} + {1} = {2}'.format(num1, num2, total));

	# Lazy proeprty
	c = Calculator();
	logger.info('Pi is {0}'.format(c.pi));

	# Warriors
	w1 = Warrior(20, 30);
	w2 = Warrior(30, 30);
	# Not define, but does not complain :S
	if(w1 >= w2):
		logger.info('Warrior 1 wins');
	else:
		logger.info('Warrior 2 wins');

if __name__ == "__main__":
	main();
