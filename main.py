import json

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} кушает.")

class Bird(Animal):
    def __init__(self, name, age, feather_color):
        super().__init__(name, age)
        self.feather_color = feather_color

    def make_sound(self):
        print(f"{self.name}: Chirp, chirp")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name}: Meow, meow")

class Reptile(Animal):
    def __init__(self, name, age, shell_color):
        super().__init__(name, age)
        self.shell_color = shell_color

    def make_sound(self):
        print(f"{self.name}: Squeak, squeak")

class ZooKeeper:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

class Veterinarian:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

class Zoo:
    def __init__(self, animals, zookeepers, veterinarians):
        self.animals = animals
        self.zookeepers = zookeepers
        self.veterinarians = veterinarians

def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def main():
    bird = Bird("Parrot", 3, "green")
    mammal = Mammal("Cat", 5, "black")
    reptile = Reptile("Turtle", 10, "brown")

    zookeeper = ZooKeeper("John", 30)
    veterinarian = Veterinarian("Dr. Smith", 40)

    animals = [bird, mammal, reptile]
    zookeepers = [zookeeper]
    veterinarians = [veterinarian]

    zoo = Zoo(animals, zookeepers, veterinarians)

    while True:
        print("\nМеню:")
        print("1. Показать всех животных")
        print("2. Добавить новое животное")
        print("3. Редактировать животное")
        print("4. Удалить животное")
        print("5. Показать всех смотрителей")
        print("6. Добавить нового смотрителя")
        print("7. Редактировать смотрителя")
        print("8. Удалить смотрителя")
        print("9. Показать всех ветеринаров")
        print("10. Добавить нового ветеринара")
        print("11. Редактировать ветеринара")
        print("12. Удалить ветеринара")
        print("13. Демонстрация работы методов")
        print("14. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            for animal in zoo.animals:
                print(f"{animal.name}, {animal.age} years old")
        elif choice == '2':
            # Add logic to add a new animal
            pass
        elif choice == '3':
            # Add logic to edit an existing animal
            pass
        elif choice == '4':
            # Add logic to remove an animal
            pass
        elif choice == '5':
            for zookeeper in zoo.zookeepers:
                print(f"{zookeeper.name}, {zookeeper.age} years old")
        elif choice == '6':
            # Add logic to add a new zookeeper
            pass
        elif choice == '7':
            # Add logic to edit an existing zookeeper
            pass
        elif choice == '8':
            # Add logic to remove a zookeeper
            pass
        elif choice == '9':
            for vet in zoo.veterinarians:
                print(f"{vet.name}, {vet.age} years old")
        elif choice == '10':
            # Add logic to add a new veterinarian
            pass
        elif choice == '11':
            # Add logic to edit an existing veterinarian
            pass
        elif choice == '12':
            # Add logic to remove a veterinarian
            pass
        elif choice == '13':
            # Demonstrate method functionality, e.g., make animals make sounds
            for animal in zoo.animals:
                animal.make_sound()
        elif choice == '14':
            print("Выход")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()