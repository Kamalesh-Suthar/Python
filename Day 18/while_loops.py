# current_number = 1
#
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. "
#
# message = ""
# while message != "quit":
#     message = input(prompt)
#     if message != "quit":
#         print(message)

# active = True
#
# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. "
#
# while active:
#     message = input(prompt)
#     if message == "quit":
#         active = False
#     else:
#         print(message)

# active = True
#
# prompt = "\nPlease enter the name of a city you have visited: "
# prompt += "\n(Enter 'quit' when you are finished.) "
#
# while active:
#     city = input(prompt)
#     if city == 'quit':
#         active = False
#     else:
#         print(f"\nI'd love to go to {city.title()}!")

# current_number = 0
#
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# unconfirmed_users = ['kamalesh', 'jatin', 'narpath']
# confirmed_users = []
#
# while unconfirmed_users:
#     name = unconfirmed_users.pop()
#     print(f"Verifying user: {name.title()}")
#     confirmed_users.append(name)
#
# print("\nThe following users were confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())
