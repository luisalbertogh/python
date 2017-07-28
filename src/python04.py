"""
python04.py

Python classes 04.
author: luisalbertogh@hotmail.com
"""

# Abstract classes
import collections.abc;
from abc import ABCMeta, abstractmethod;

# Take times
import timeit;

# Extend Callable abstract class
class Creature(collections.abc.Callable):
	def __call__(self, arg):
		print('Grunt! ',arg);

#Abstract class
class Picasso(metaclass=ABCMeta):
	# Abstract method
	@abstractmethod
	def paint(self):
		pass;

	# Class method
	@classmethod
	def eat(self):
		print('yummy');

# Extend abstract class
class Painter(Picasso):
	def paint(self):
		print('No thanks');

# Context
class Museum:
	def __init__(self, ticket):
		if(ticket):
			self.granted = True;
		else:
			self.granted = False;

	def __enter__(self):
		if(self.granted):
			print('Welcome to the musem');
		else:
			print('Sorry, you need a ticket');

	def __exit__(self, exc_type, exc_value, traceback):
		print('Bye');		

"""
Main method
"""
def main():
	# Is instanceof
	c = Creature();
	if(isinstance(c, collections.abc.Callable)):
		print('It is Callable');
		c('Luis');
	else:
		print('It is NOT Callable');

	# Class from abstract
	p = Painter();
	p.paint();

	# Context
	with Museum(True):
		pass;

if __name__ == "__main__":
	main();
