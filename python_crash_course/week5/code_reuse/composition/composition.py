
class Repository:
	def __init__(self):
		self.packages = {}
	def add_package(self, package):
		self.packages[package.name] = package
	def del_package(self, package):
		del self.packages[package.name]
	def total_size(self):
		result = 0
		for package in self.packages.values():
			result += package.size
		return result

class Clothing():
	stock = {"name":[], "material":[], "amount":[]}
	def __init__(self, name):
		material = ""
		self.name = name
	def add_item(self, name, material, amount):
		self.stock["name"].append(self.name)
		self.stock["material"].append(self.material)
		self.stock["amount"].append(amount)
	def stock_by_material(self, material):
		count = 0
		n = 0
		for item in self.stock["material"]:
			if item == material:
				count += self.stock["amount"][n]
				n += 1
		return count

class Shirt(Clothing):
	material = "Cotton"

class Pants(Clothing):
	material = "Wool"

polo = Shirt("Polo")
polo.add_item(polo.name, polo.material, 6)
polo.add_item(polo.name, polo.material, 6)
print(polo.name)
print(polo.material)
polo_current_stock = polo.stock_by_material("Cotton")
print(polo_current_stock)

sweatpants = Pants("Sweatpants")
print(sweatpants.name)
print(sweatpants.material)
sweatpants.add_item(sweatpants.name, sweatpants.material, 3)
sweatpants.add_item(sweatpants.name, sweatpants.material, 3)
sweatpants_current_stock = sweatpants.stock_by_material("Wool")
print(sweatpants_current_stock)

