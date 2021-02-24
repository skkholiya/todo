#class: is a blueprint of an object. An Object that holds the methods and properties. Object can be any real world entity.
 
#__init__() method in python is work same as the constructor in java or c++, to initalize properties of the object.
#__init__(self): it basically refer the current object.name can be anything.


# Protected member: by using (_) single underscore before attribute name.

# Private member: (__) before the method/variable name.

class Person:
	@staticmethod #common for all the class objects. doesn't depends on the object creation. 
	def companyName(company="Vaco"):
		return company;
	
	def __init__(this,__age,name,city):
		this.__age = __age;
		this.name = name;
		this.city = city;
	#Accessing class private properties.(OOPS feature Encapsulation)
	def getAge(this):
		return this.__age;

class Address:
  #pass statement use when the class has no content, basically avoid errors.
  pass;

p = Person(34,"simran","jaipur");
p1 = Person(45,"kiran","kota");
address = Address();
#Accessing properties
print("Accessing Object property:",p.name);
#Accessing Object private properties
print("Accessing Object private property",p.getAge());

#get all properties in dict format
print("person 1", p1.__dict__)
print("address class object:", address.__dict__);

#Modifiying Object Properties.
p.name = "Raj";
print("Modifing Object Property:",p.name);

#Deleting Object Properties.
print("before deleting:",p.city);
del p.city;

#Deleting Object
print("deleted person object p1:");
del p1;

#accessing static method
print(Person.companyName());

#accessing static method using reference
print(p.companyName("binary semantic"));


