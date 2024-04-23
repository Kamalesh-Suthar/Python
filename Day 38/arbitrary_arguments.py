# def make_pizza(*toppings):
#     """Summarize the pizza about to be made"""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f" - {topping}")
#
# make_pizza('pepperoni')
# make_pizza('pepperoni', 'extra cheese', 'mushrooms')

# def make_pizza(size, *toppings):
#     """Summarize the pizza to be made."""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
#
# make_pizza(11, 'pepperoni')
# make_pizza(11, 'pepperoni', 'extra cheese', 'mushrooms')

def build_profile(first, last, **user):
    user['first_name'] = first
    user['last_name'] = last
    print(user)
    return user


# build_profile('albert', 'einstein', location='New York')
