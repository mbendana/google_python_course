# Create a class Apple and then an instance of it to use it
class Apple:
	def __init__(self, color, flavor):
		self.color = color
		self.flavor = flavor
	def __str__(self):
		return f"The color of this apple is {self.color} and its flavor is {self.flavor}."

jonagold = Apple("red", "sweet")
print(f"The jonagold apple color is {jonagold.color} and the jonagold apple flavor is {jonagold.flavor}")
print(jonagold)

# Create a class Person and then an instance of it to use it
class Person:
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return f"The name of this person is {self.name}."
	def greeting(self):
		return f"Hi, my name is {self.name}"

# Create a new Person class instance with a name of your choice
name = Person("Scarlett")
print(name.greeting())
print(name)
