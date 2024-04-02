# pizza = {
#     'crust': 'thick',
#     'toppings': ['pepperoni', 'mushrooms', 'jalapeno', 'extra cheese'],
# }
#
# print(f"You ordered a pizza with a {pizza['crust']}-crust pizza "
#       "with the following toppings:")
#
# for topping in pizza['toppings']:
#     print(f"\t {topping.title()}")

# favorite_languages = {
#     'kamalesh': ['javsscript', 'c++', 'java', 'python'],
#     'narpath': ['javascript', 'c++'],
#     'jatin': ['javascript', 'c'],
# }
#
# for person in favorite_languages.keys():
#     print(f"{person.title()}'s favorite languages are:")
#     for language in favorite_languages[person]:
#         print(f"\t {language.title()}")
#
# for person, languages in favorite_languages.items():
#     print(f"\n{person.title()}'s favorite languages are:")
#     for language in languages:
#         print(f"\t{language.title()}")

# users = {
#     'suthar': {
#         'first': 'kamalesh',
#         'last': 'suthar',
#         'location': 'bangalore',
#         },
#
#     'jatin': {
#         'first': 'jatin',
#         'last': 'suthar',
#         'location': 'chennai'
#     },
# }
#
# for user, info in users.items():
#     print(f"\nUsername: {user.title()}")
#     full_name = f"{info['first']} {info['last']}"
#     location = info['location']
#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")