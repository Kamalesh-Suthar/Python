# Good idea to always name lists in plurals variable names as they contain multiple types/number of data

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[0])
# print(bicycles[0].title())
# print(bicycles[1])
# print(bicycles[3])
# print(bicycles[-1])

# message_1 = f"My first bicycle was a {bicycles[0]}."
# print(message_1)

# 3.1
# names = ["Jatin", "Naresh", "Lalit"]
# print(names[0])
# print(names[1])
# print(names[-1])

# 3.2
# greeting_1 = f"Hello, {names[0]}"
# greeting_2 = f"Konichiva {names[1]}"
# greeting_3 = f"Hi there, {names[-1]}"

# print(greeting_1)
# print(greeting_2)
# print(greeting_3)

# motorcycles = ["splendor", 'duke 200', 'ninja', 'pulsar']
# print(motorcycles)
# motorcycles[-1] = 'bmw'
# print(motorcycles)
# motorcycles.append('pulsar')
# print(motorcycles)

new_empty_list = []
new_empty_list.append('Jatin')
new_empty_list.append('Naresh')
new_empty_list.append('Lalit')
print(new_empty_list)
new_empty_list.insert(0, 'Kamalesh')
print(new_empty_list)

# del new_empty_list[-1]
# remove() only deletes/removes the first occurance of the value in a given list

# removed_value = new_empty_list.pop()

# removed_value = new_empty_list.pop(-1)
# print(removed_value)

# print(f"{removed_value.title()} is a good friend of mine.")
# new_empty_list.remove('Lalit')

# less_friendlier = 'Lalit'
# new_empty_list.remove(less_friendlier)
# print(f"{less_friendlier.title()} is less friendlire to me.")
print(new_empty_list)

