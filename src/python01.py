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
		print('');

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
	Set behaviour.
	"""
	def setBehave(self, behave):
		self.behave = behave;

	"""
	Print superhero details.
	"""
	def printHero(self):
		print(self.gender + '; ' + self.race + '; ' + self.behave);

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
	def show(self):
		for xman in self:
			xman.printHero();

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
	def show(self):
		for xman in self.xmen:
			xman.printHero();

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
	xplanet.show();

	# Rules
	frules = FightRules();
	print(frules.win(SuperHero('male','man','good'), SuperHero('female','martian','good')));

if __name__ == "__main__":
	main();
