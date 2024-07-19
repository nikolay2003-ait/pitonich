import random

class Animal:
    def __init__(self, species, size, food_type, habitat, lifespan):
        self.species = species
        self.size = size
        self.food_type = food_type
        self.habitat = habitat
        self.lifespan = lifespan
        self.age = 0
        self.satiety = 100  # Начальная сытость 100%
        self.gender = random.choice(['male', 'female'])

    def __str__(self):
        return f"{self.species} - Age: {self.age}, Satiety: {self.satiety}%, Gender: {self.gender}"

class Ecosystem:
    def __init__(self):
        self.animals = []
        self.plant_food = 1000  # Начальный запас растительной пищи

    def add_animal(self, animal):
        self.animals.append(animal)

    def increase_plant_food(self, amount):
        self.plant_food += amount

    def display_animals(self):
        for animal in self.animals:
            print(animal)

    def simulate_time_step(self):
        deceased_animals = []
        for animal in self.animals:
            animal.age += 1
            if animal.food_type == "herbivore":
                if self.plant_food > 0:
                    self.plant_food -= 1
                    animal.satiety += 26
                else:
                    animal.satiety -= 9
            elif animal.food_type == "carnivore":
                if random.random() < 0.5:
                    prey = self.find_prey(animal)
                    if prey:
                        self.animals.remove(prey)
                        animal.satiety += 53
                        deceased_animals.append((prey, "eaten"))
                    else:
                        animal.satiety -= 16
                else:
                    animal.satiety -= 16
            elif animal.food_type == "omnivore":
                if self.plant_food > 0:
                    self.plant_food -= 1
                    animal.satiety += 26
                else:
                    animal.satiety -= 9
                if random.random() < 0.5:
                    prey = self.find_prey(animal)
                    if prey:
                        self.animals.remove(prey)
                        animal.satiety += 53
                        deceased_animals.append((prey, "eaten"))
                    else:
                        animal.satiety -= 16
                else:
                    animal.satiety -= 16

            if animal.age >= animal.lifespan:
                deceased_animals.append((animal, "age"))
            elif animal.satiety < 10:
                deceased_animals.append((animal, "starvation"))

        for animal, reason in deceased_animals:
            if reason != "eaten":
                self.animals.remove(animal)
                self.plant_food += animal.size
            if reason == "age":
                print(f"{animal.species} died of old age at age {animal.age}.")
            elif reason == "starvation":
                print(f"{animal.species} died of starvation with satiety {animal.satiety}%.")
            elif reason == "eaten":
                print(f"{animal.species} was eaten.")

    def find_prey(self, predator):
        possible_prey = [animal for animal in self.animals if animal.food_type == "herbivore"]
        if possible_prey:
            return random.choice(possible_prey)
        return None

    def reproduce(self, parent1, parent2):
        if parent1.species == parent2.species and parent1.gender != parent2.gender:
            if parent1.habitat == "water" and parent1.satiety > 50 and parent2.satiety > 50:
                self.animals.extend([Animal(parent1.species, parent1.size, parent1.food_type, parent1.habitat, parent1.lifespan) for _ in range(10)])
            elif parent1.habitat == "air" and parent1.satiety > 42 and parent1.age > 3 and parent2.age > 3:
                self.animals.extend([Animal(parent1.species, parent1.size, parent1.food_type, parent1.habitat, parent1.lifespan) for _ in range(4)])
            elif parent1.habitat == "land" and parent1.satiety > 20 and parent1.age > 5 and parent2.age > 5:
                self.animals.extend([Animal(parent1.species, parent1.size, parent1.food_type, parent1.habitat, parent1.lifespan) for _ in range(2)])

    def menu(self):
        while True:
            print("\n--- Menu ---")
            print("1. Display all animals")
            print("2. Add animal")
            print("3. Increase plant food")
            print("4. View animal characteristics")
            print("5. Simulate reproduction")
            print("6. Simulate time step")
            print("7. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.display_animals()
            elif choice == '2':
                self.add_animal_from_input()
            elif choice == '3':
                amount = int(input("Enter the amount of plant food to add: "))
                self.increase_plant_food(amount)
            elif choice == '4':
                self.view_animal_characteristics()
            elif choice == '5':
                self.simulate_reproduction()
            elif choice == '6':
                self.simulate_time_step()
            elif choice == '7':
                break
            else:
                print("Invalid choice, please try again.")

    def add_animal_from_input(self):
        species = input("Enter species name: ")
        existing_animal = next((animal for animal in self.animals if animal.species == species), None)
        if existing_animal:
            animal = Animal(existing_animal.species, existing_animal.size, existing_animal.food_type, existing_animal.habitat, existing_animal.lifespan)
            self.add_animal(animal)
        else:
            size = int(input("Enter size: "))
            food_type = input("Enter food type (herbivore/carnivore/omnivore): ")
            habitat = input("Enter habitat (water/air/land): ")
            lifespan = int(input("Enter lifespan: "))
            animal = Animal(species, size, food_type, habitat, lifespan)
            self.add_animal(animal)

    def view_animal_characteristics(self):
        species = input("Enter species name to view characteristics: ")
        for animal in self.animals:
            if animal.species == species:
                print(animal)

    def simulate_reproduction(self):
        species = input("Enter species name for reproduction: ")
        parents = [animal for animal in self.animals if animal.species == species]
        if len(parents) >= 2:
            self.reproduce(parents[0], parents[1])
        else:
            print("Not enough animals of the specified species to reproduce.")

# Создание начальных видов животных
ecosystem = Ecosystem()
species_list = [
    ("Fish", 5, "herbivore", "water", 10),
    ("Bird", 3, "herbivore", "air", 6),
    ("Lion", 50, "carnivore", "land", 12),
    ("Deer", 30, "herbivore", "land", 15),
    ("Shark", 100, "carnivore", "water", 20),
    ("Eagle", 6, "carnivore", "air", 10),
    ("Rabbit", 2, "herbivore", "land", 5),
    ("Frog", 1, "omnivore", "water", 4),
    ("Bee", 0.1, "herbivore", "air", 2),
    ("Wolf", 40, "carnivore", "land", 14),
    ("Turtle", 10, "herbivore", "water", 50),
    ("Owl", 4, "carnivore", "air", 8)
]

for species in species_list:
    ecosystem.add_animal(Animal(*species))

# Запуск меню
ecosystem.menu()
