"""
python03.py

Python classes 03.
author: luisalbertogh@hotmail.com
"""

# Abstract classes
import abc;

# Garbage collector
import gc;

#Weak references for cyclic relations
import weakref;

"""
Sportman superclass with init method.
"""
class Sportbeing(metaclass=abc.ABCMeta):
	"""
	Init method.
	"""
	def __init__(self, gender, nationality):
		self.gender = gender;
		self.nationality = nationality;

	#@abstractmethod
	def show(self):
		pass;

"""
Subclass extends from superclass.
"""
class Cyclist(Sportbeing):
	"""
	Init method.
	"""
	def __init__(self, gender, nationality, name):
		# Invoke superclass init
		super().__init__(gender, nationality);
		self.name = name;

	"""
	Static mehod to create instances.
	"""
	@staticmethod
	def createInstance():
		return Cyclist('male','Spanish','Valverde');

	"""
	Set name.
	"""
	def setName(self, team):
		self.name = name;

	"""
	Print instance details (used in print).
	"""
	def __str__(self):
		return self.gender + '; ' + self.nationality + '; ' + self.name;

	"""
	Format instance details.
	"""
	def __format__(self, spec):
		return self.gender + '; ' + self.nationality + '; ' + self.name;

	"""
	Print instance details.
	"""
	def __repr__(self):
		return "{0}:{1}".format(self.__class__, self.gender + '; ' + self.nationality + '; ' + self.name);

	"""
	Override equlas method
	"""
	def __eq__(self, other):
		if(not isinstance(other, Cyclist)):
			return NotImplemented;

		return (self.gender == other.gender and self.nationality == other.nationality and self.name == other.name);

	"""
	Override hash method
	"""
	def __hash__(self):
		return hash(self.gender) ^ hash(self.nationality) ^ hash(self.name);

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
class Team(list):
	"""
	Init method.
	"""
	def __init__(self, name, *team):
		super().__init__(list(team));
		for rider in self:
			rider.parent = weakref.ref(self);
		self.name = name;

	"""
	Print team
	"""
	def __str__(self):
		riders = self.name + ':\n';
		for rider in self:
			riders = riders + rider.__str__() + ';';
		return riders;

	"""
	Override __bool__ method.
	"""
	#def __bool__(self):
	#	return super().__bool__(self);

"""
Composed class.
"""
class Tour:
	"""
	Init method.
	"""
	def __init__(self, *team):
		self.team = list(team);

	"""
	Print tour
	"""
	def __str__(self):
		riders = '';
		for riders in self.team:
			riders = riders + rider.__str__() + ';';
		return riders;

"""
Strategy class (stateless, no data, only logic).
"""
class StageRules:
	def win(self, rider1, rider2):
		return True;

	def lose(self, rider1, rider2):
		return False;


"""
Main method
"""
def main():
	team = Team('Movistar', Cyclist('male','Spanish','Valverde'), Cyclist('male','Colombian','Quintana'), Cyclist('male','Basque','Izagirre'));
	print(team);
	team = Team('Sky', Cyclist('male','Basque','Landa'), Cyclist('male','Colombian','Henao'), Cyclist('male','Kenian','Froom'));
	print(team);
	
if __name__ == "__main__":
	main();
