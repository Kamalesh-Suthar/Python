# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#
# print(contents.rstrip())

# file_name = 'pi_digits.txt'
# with open(file_name) as file_obj:
#     lines = file_obj.readlines()
#
# # for line in lines:
# #     print(line.rstrip())
#
# pi_string = ""
# for line in lines:
#     pi_string += line.strip()
#
# print(len(pi_string))

file_name = "programming.txt"
with open(file_name, "w") as file_obj:
    file_obj.write("Do I love programming anymore?!\n")
    file_obj.write("Well, I'm no more sure about this one. You caught me up there.\n")