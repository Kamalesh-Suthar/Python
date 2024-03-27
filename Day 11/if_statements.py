# Simple if statement
# if True:
#     print("Hello World")

# age = 22
# if age >= 18:
#     print("You are old")
#     print("Have you registered to vote yet?")

# age = 17
# if age >= 18:
#     print("You are old enough to vote!")
#     print("Have you registered to vote yet?")
# else:
#     print("Sorry, you are too young to vote.")
#     print("Please register to vote as soon as you turn 18!")

# age = 12
#
# if age < 4:
#     # print("Your admission cost is $0.")
#     price = 0
# elif age < 18:
#     # print("Your admission cost is $25.")
#     price = 25
# else block is not mandatory in Python
# else:
#     # print("Your admission cost is $40.")
#     price = 40
# print(f"Your admission cost is ${price}.")

# Checking multiple conditions
#
# requested_toppings = ['mushrooms', 'extra cheese']
#
# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni")

# requested_toppings = ['mushrooms', 'paneer', 'cheese', 'green peppers', 'jalapenos', 'extra cheese']
# requested_toppings = []
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         if requested_topping == 'green peppers':
#             print("Sorry, we are out of green peppers right now!")
#         else:
#             print(f"Adding {requested_topping}.")
# else:
#     print("Are you sure you want a plain pizza?!")
#
# print("\nFinished making the pizza!")

# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
#
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adding {requested_topping}")
#     else:
#         print(f"Sorry, we do not have {requested_topping}")
# print("\nFinished making your pizza!")

