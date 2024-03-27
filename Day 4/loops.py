# magicians = ['kamalesh', 'jatin', 'naresh', 'lalit']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}\n")
#
# print("Thank you, everyone. That was a great magic show!")

# for value in range(1, 10):
#     print(value)
#
# for value in range(1, 11):
#     print(value)

# numbers = list(range(1,6))
# print(numbers)

# numbers = list(range(2, 11, 2))
# print(numbers)

# squares  = []
# for number in range(1, 11):
#     squares.append(number ** 2)
#
# print(squares)
#
# print(min(squares))
# print(max(squares))
# print(sum(squares))

# squares = [value ** 2 for value in range(1, 11)]
# print(squares)
#
# cubes = [value ** 3 for value in range(1, 6)]
# print(cubes)

players = ['kamalesh', 'jatin', 'naresh', 'lalit', 'jayesh']
# print(players[0:3])
# print(players[0:-3])
# print(players[:-1])
# print(players[-3:])

# for player in players[-3:]:
#     print(player.title())

# making a copy
foods = ['pizza', 'burger', 'fries']
# foods_copy = foods[:]
# print(foods)
# print

foods_copy = foods
print(foods)
print(foods_copy)
foods_copy.append('ice cream')
print(foods)