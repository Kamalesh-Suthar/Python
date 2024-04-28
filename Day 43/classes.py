class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """simulate a dog rolling over in response to a command."""
        print(f"{self.name} is now rolling over.")


my_dog = Dog("Bob", 20)

print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age}")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog("Jack", 25)

print(f"Your dog's name is {your_dog.name}")
print(f"Your dog's age is {your_dog.age}")

your_dog.sit()