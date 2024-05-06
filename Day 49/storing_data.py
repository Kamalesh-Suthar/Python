import json

numbers = [1,2,3,4,5]

filename = 'numbers.json'

# -- write
# with open(filename, 'w') as f:
#     json.dump(numbers, f)

# -- read
with open(filename) as f:
    nums = json.load(f)

print(nums)