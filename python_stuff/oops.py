class Dog:

  def __init__(self, name, age, breed):
    self.name = name
    self.age = age
    self.breed = breed  
    self.tricks = []

  @classmethod
  def register_stuff(cls):
     return cls("Unknown", 0, "Unknown Breed")
  
  def bark(self):
    print(f"{self.name} says Woof!")

  def learn_trick(self, trick):
    self.tricks.append(trick)
    print(f"{self.name} has learned {trick}!")

  def perform_trick(self,trick):
    if trick in self.tricks:
        print(f"{self.name} performs {trick}!")
    else:
        print(f"{self.name} doesn't know that trick yet!")

NEW_dog = Dog.register_stuff()
NEW_dog.bark()
Buddy = Dog("Buddy", 3, "Golden Retriever")
Buddy.bark()
Buddy.learn_trick("roll over")
Buddy.perform_trick("sit")
Buddy.perform_trick("roll over")
