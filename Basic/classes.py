class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

p = Point(2, 8)
print(p.x)
print(p.y)



#`self` is a reference to the instance of a class that is currently being operated on. It is typically the first parameter of a method in a class, and it is used to access and modify the attribute of the instance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hi, my name is", self.name, "and I'm", self.age, "years old.")

person1 = Person("Alice", 25)
person1.introduce()

#In the introduce method, self.name and self.age are used to access the name and age attributes of the current instance (person1). When we call person1.introduce(), the self parameter is automatically set to person1.
#In summary, self is a special parameter used in class methods to refer to the instance of the class currently being operated on.



class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight succssfully.")

    else:
        print(f"No available seats for {person}")




