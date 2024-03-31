# alien = {
#     'color': 'green',
#     'points': 5
# }

# print(alien)
# print(alien['color'])
# print(alien['points'])

# alien['x_position'] = 0
# alien['y_position'] = 25
#
# print(alien)

# alien = {}
#
# alien['color'] = 'green'
# alien['points'] = 5
#
# print(alien)
#
# print(f"The alien is {alien['color']}")
# alien['color'] = 'red'
#
# print(f"The alien is now {alien['color']}")

# alien = {
#     'x_position': 0,
#     'y_position': 25,
#     'speed': 'medium',
#     'points': 10
# }
#
# if(alien['speed'] == 'slow'):
#     x_increement = 1
# elif(alien['speed'] == 'medium'):
#     x_increement = 2
# else:
#     x_increement = 3
#
# print(alien)
# alien['x_position'] = alien['x_position'] + x_increement
# print(f"The new position: {alien['x_position']}")
#
# del alien['points']
# print(alien)

# favorite_languages = {
#     'kamalesh': 'javascript',
#     'jatin': 'python',
#     'narpath': 'javascript',
#     'goutam': 'go'
# }
#
# print(f"Kamalesh's favorite language is {favorite_languages['kamalesh'].title()}")

# alien = {
#     'color': 'green',
#     'points': 25
# }
#
# points = alien.get('points', 'No points earned')
# print(points)

# user = {
#     'name': 'kamalesh',
#     'age': 22,
#     'city': 'Bangalore',
# }
#
# for key, value in user.items():
#     print(f'\nKey: {key}')
#     print(f'Value: {value}')

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
#
# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}")
#
# for keys in favorite_languages.keys():
#     print(keys.title())
#
# for name in favorite_languages:
#     print(name.title())
#
# friends = ['phil', 'jatin']
# for name in favorite_languages.keys():
#     print(name.title())
#
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}'s favorite language is {language}")