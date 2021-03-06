"""
python01.py

Python classes 01.
author: luisalbertogh@hotmail.com
"""

# Abstract classes
import abc;

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
	Print superhero details.
	"""
	def __str__(self):
		return self.gender + '; ' + self.race + '; ' + self.behave;

	"""
	Print superhero details.
	"""
	def __repr__(self):
		return __class__ + '.' + __name__ + self.gender + '; ' + self.race + '; ' + self.behave;

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
		#self.xmen = [SuperHero('male','man','good'), SuperHero('female','martian','good'), SuperHero('male','ET','evil')];

	"""
	Print Xmen
	"""
	def __str__(self):
		allxmen = '';
		for xman in self:
			allxmen = allxmen + xman.str() + ';';

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
			allxmen = allxmen + xman.str() + ';';

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
	xmen = Xmen();

	# Xplanet
	xplanet = Xplanet(xmen.pop(), xmen.pop());
	#xplanet.show();

	# Rules
	frules = FightRules();
	#print(frules.win(SuperHero('male','man','good'), SuperHero('female','martian','good')));

	# Use static methods
	print(SuperHero.createSH());

if __name__ == "__main__":
	main();
