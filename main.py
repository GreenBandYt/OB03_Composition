# Home Work 3
# Author: Yuriy Bandura

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        self.make_sound()

    def eat(self):
        print(f"{self.name} is eating.")

    def feed(self):
        print(f"{self.name} is feeding.")

    def heal(self):
        print(f"{self.name} is healing.")

class Bird(Animal):
    def __init__(self, name, age, feather_color):
        super().__init__(name, age)
        self.feather_color = feather_color
    def make_sound(self):
        print("Chirp, chirp")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color
    def make_sound(self):
        print("Meow, meow")

class Reptile(Animal):
    def __init__(self, name, age, shell_color):
        super().__init__(name, age)
        self.shell_color = shell_color
    def make_sound(self):
        print("Squeak, squeak")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

def animal_eat(animals):
    for animal in animals:
        animal.eat()

class Zoo:
    def __init__(self, animals, zookeepers, veterinarians):
        self.animals = animals
        self.zookeepers = zookeepers
        self.veterinarians = veterinarians

class ZooKeeper:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def feed_animal(self, animal):
        animal.feed()


class Veterinarian:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def heal_animal(self, animal):
        animal.heal()

bird = Bird("Parrot", 2, "Green")
mammal = Mammal("Cat", 3, "Black")
reptile = Reptile("Turtle", 5, "Brown")

zookeeper = ZooKeeper("John", 30)
veterinarian = Veterinarian("Jane", 35)

zoo = Zoo([bird, mammal, reptile], [zookeeper], [veterinarian])


animals = [bird, mammal, reptile]
animal_sound(animals)
animal_eat(animals)

for animal in animals:
    zookeeper.feed_animal(animal)
    veterinarian.heal_animal(animal)

