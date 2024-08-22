class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

def animal_speak(animal):
    return animal.speak()


dog = Dog()
cat = Cat()

print(animal_speak(dog))
print(animal_speak(cat))