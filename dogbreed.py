class Dog:
    animal = "Dog"
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
    def display_details(self):
        print(f"Animal: {Dog.animal}")
        print(f"Breed: {self.breed}")
        print(f"Color: {self.color}")
        print("-" * 30)
dog1 = Dog("German Shepherd", "Black and Tan")
dog2 = Dog("Golden Retriever", "Golden")
dog1.display_details()
dog2.display_details()