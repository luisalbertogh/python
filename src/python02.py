"""
python02.py

Python classes 02.
author: luisalbertogh@hotmail.com
"""

# Abstract classes
import abc;

# Garbage collector
import gc;

#Weak references for cyclic relations
import weakref;

"""
Hero superclass with init method.
"""
class Hero(metaclass=abc.ABCMeta):
	"""
	Init method.
	"""
	def __init__(self, gender, race):
		self.gender = gender;
		self.race = race;

	#@abstractmethod
	def show(self):
		pass;

"""
Subclass extends from superclass.
"""
class SuperHero(Hero):
	"""
	Init method.
	"""
	def __init__(self, gender, race, behave):
		# Invoke superclass init
		super().__init__(gender, race);
		self.behave = behave;

	"""
	Static mehod to create Superheroes.
	"""
	@staticmethod
	def createSH():
		return SuperHero('male','man','good');

	"""
	Set behaviour.
	"""
	def setBehave(self, behave):
		self.behave = behave;

	"""
	Print superhero details (used in print).
	"""
	def __str__(self):
		return self.gender + '; ' + self.race + '; ' + self.behave;

	"""
	Format superhero details.
	"""
	def __format__(self, spec):
		return self.gender + '; ' + self.race + '; ' + self.behave;

	"""
	Print superhero details.
	"""
	def __repr__(self):
		return "{0}:{1}".format(self.__class__, self.gender + '; ' + self.race + '; ' + self.behave);

	"""
	Override equlas method
	"""
	def __eq__(self, other):
		if(not isinstance(other, SuperHero)):
			return NotImplemented;

		return (self.gender == other.gender and self.race == other.race and self.behave == other.behave);

	"""
	Override hash method
	"""
	def __hash__(self):
		return hash(self.gender) ^ hash(self.race) ^ hash(self.behave);

	"""
	Invoked when destroying the object.
	- Use it to close files and end up resouces used within the current class
	"""
	def __del__(self):
		print('Removing {0}'.format(id(self)));

	"""
	Print parent.
	"""
	def printParent(self):
		p = self.parent();
		if(p is not None):
			print(p);
		else:
			print('No parent found!');


"""
More classes.
It inherits from 'list' class.
"""
class Xmen(list):
	"""
	Init method.
	"""
	def __init__(self):
		super().__init__([SuperHero('male','man','good'), SuperHero('female','martian','good'), SuperHero('male','ET','evil')]);
		for xman in self:
			xman.parent = weakref.ref(self);
		#self.xmen = [SuperHero('male','man','good'), SuperHero('female','martian','good'), SuperHero('male','ET','evil')];

	"""
	Print Xmen
	"""
	def __str__(self):
		allxmen = '';
		for xman in self:
			allxmen = allxmen + xman.__str__() + ';';
		return allxmen;

	"""
	Override __bool__ method.
	"""
	#def __bool__(self):
	#	return super().__bool__(self);

"""
Composed class.
"""
class Xplanet:
	"""
	Init method.
	"""
	def __init__(self, *xmen):
		self.xmen = list(xmen);

	"""
	Print Xmen
	"""
	def __str__(self):
		allxmen = '';
		for xman in self.xmen:
			allxmen = allxmen + xman.__str__() + ';';
		return allxmen;

"""
Strategy class (stateless, no data, only logic).
"""
class FightRules:
	def win(self, xman1, xman2):
		return True;

	def lose(self, xman1, xman2):
		return False;


"""
Main method
"""
def main():
	# Xmen
	#xmen = Xmen();

	# Xplanet
	#xplanet = Xplanet(xmen.pop(), xmen.pop());
	#xplanet.show();

	# Rules
	#frules = FightRules();
	#print(frules.win(SuperHero('male','man','good'), SuperHero('female','martian','good')));

	# Use static methods
	#print(SuperHero.createSH().__format__());
	#print('This is a superhero: {0}'.format(SuperHero.createSH()));

	# Compare
	sh1 = SuperHero('male','man','good');
	sh2 = SuperHero('male','man','good');
	#print(hash(sh1), hash(sh2));
	if(sh1 == sh2):
		print('EQUALS');
	else:
		print('DIFFERENT');

	# Bool
	xmen = Xmen();
	if(xmen):
		print('Hay Xmen...');
		#del(xmen);
		for xman in xmen:
			xman.printParent();

	# GC
	gc.collect();
	gc.garbage;

if __name__ == "__main__":
	main();
