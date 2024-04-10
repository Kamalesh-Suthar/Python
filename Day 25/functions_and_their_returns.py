# def build_person(first_name, last_name, age = None):
#     """Returns a dictionary of information about a person"""
#     person = {
#         'first_name': first_name,
#         'last_name': last_name,
#         'full_name': f"{first_name} {last_name}"
#     }
#     if age:
#         person['age'] = age
#     return person
#
# person = build_person('kamalesh', 'suthar')
# person = build_person('kamalesh', 'suthar', 23)
# print(person)

# def get_formatted_value(first_name, last_name):
#     """Returns a neatly formatted full name"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
# while True:
#     print("\nPlease tell me your name")
#     print("\nEnter 'q' to quit")
#
#     f_name = input("\tFirst name: ")
#     if f_name == 'q':
#         break
#
#     l_name = input("\tLast name: ")
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_value(f_name, l_name)
#     print(f"\nHello {formatted_name}")


# def greet_user(names):
#     """Print a simple greeting to the users"""
#     for name in names:
#         print(f"Hello, {name.title()}!")
#
#
# users = ['kamalesh', 'jatin', 'naresh', 'lalit']
# greet_user(users)


# def print_models(unprinted_models, completed_models):
#     """
#     Simulate printing each design until none are left.
#     Move each design to completed models after printing
#     """
#     while unprinted_models:
#         current_model = unprinted_models.pop()
#         print(f"Printing model: {current_model}")
#         completed_models.append(current_model)
#
# def show_completed_models(completed_models):
#     """Prints all the completed models"""
#     print("\nThe following models have been completed")
#     for completed_model in completed_models:
#         print(f"Model: {completed_model}")
#
#
# unprinted_designs = ['phone case', 'robot pendent', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)
# print(unprinted_designs)

