# Create an Apple class and an instance of it
class Apple:
	def __init__(self, color, flavor):
		self.color = color
		self.flavor = flavor
	def __str__(self):
		return f"The color of this apple is {self.color} and its flavor is{self.flavor}."

#help(Apple)

def to_seconds(hours, minutes, seconds):
	"""Returns the amount of seconds in the given hours, minutes and seconds."""
	return hours * 3600 + minutes * 60 + seconds

#help(to_seconds)

class Piglet:
	"""Represents a piglet that can say its name."""
	years = 0
	name = ""
	def speak(self):
		"""Outputs a message including the name of the piglet."""
		print("Oink! I'm {}! Oink!".format(self.name))
	def pig_years(self):
		"""Converts the current age to equivalent piglet years."""
		return self.years * 18

help(Piglet)
