
class Fruit:
	def __init__(self, color, flavor):
		self.color = color
		self.flavor = flavor

class Apple(Fruit):
	pass

class Grape(Fruit):
	pass

my_dad = Apple("black", "sour")
my_mom = Grape("pink", "bittersweet")

#print(f"My dad's apple's color is {my_dad.color} and its flavor is {my_dad.flavor}")
#print(f"My mom's grape's color is {my_mom.color} and its flavor is {my_mom.flavor}")

class Animal():
	sound = ""
	def __init__(self, name):
		self.name = name
	def speak(self):
		print("{sound} I'm {name}! {sound}".format(sound = self.sound, name = self.name))

class Piglet(Animal):
	sound = "Oink!"

hamlet = Piglet("Hamlet")
print(f"The name of the piglet is {hamlet.name} and it can say: ", end="")
hamlet.speak()

class Clothing():
	material = ""
	def __init__(self, name):
		self.name = name
	def check_material(self):
		print("This {} is made of {}".format(self.name, self.material))

class Shirt(Clothing):
	material = "Cotton"

polo = Shirt("Polo")
polo.check_material()
