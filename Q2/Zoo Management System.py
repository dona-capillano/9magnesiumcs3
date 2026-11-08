class Animals:  #creates class
  def __init__(self, name):
      self.name = name
  def make_sound(self):
      pass
  def eat(self):
      pass

class Lion(Animal):
  def make_sound(self):
      def make_sound(self):
          return f"{self.name} raors loudly!"
      def eat(self):
          return f"{self.name} eats fresh meat."

class Elephant(Animal):
  def make_sound(self):
    return f"{self..name} trumpets!"
  def eat(self):
    return f"{self.name} eats grass and fruits."

class Monkey(Animal):
  def make_sound(self):
    return f"{self.name} chatters!
  def eat(self): 
    return f"{self.name} eats bananas."

if __name__ == "__main__":
  animals = [Lion("Simba"), Elephant ("Dumbo"), Monkey("George")]

  for animal in animals:
      print(animal.make_sound())
      print(animal.eat())
      print("-----")
