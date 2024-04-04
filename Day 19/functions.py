# def greet_user():
#     # docstring - used for documentation internally by Python
#     """Display a simple greeting."""
#     print("Hello!")
#
# greet_user()

# def greet_user(username):
#     """Displays a simple greeting."""
#     print(f"Hello, {username.title()}!")
#
# greet_user('kamalesh')

# Positional Arguments
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willy')


# Keyword Arguments
# def describe_pet(animal_type, pet_type):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_type.title()}.")
#
# describe_pet(animal_type='dog', pet_type='junior')

# Default values
# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
# describe_pet('Willd')

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name =  f"{first_name} {last_name}"
#     return full_name.title()
#
# musician = get_formatted_name('Jonathan', 'larson')
# print(musician)

# def get_formatted_name(first_name, last_name, middle_name = ""):
#     """Return a full name, neatly formatted."""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
# player = get_formatted_name('kamalesh', 'suthar')
# player = get_formatted_name('kamalesh', 'suthar', 'lee')
# print(player)