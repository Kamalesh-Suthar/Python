file_name = "programming.txt"

with open(file_name, "a") as file_obj:
    file_obj.write("Adding a line: _Hello World!_\n")
    file_obj.write("Done.\n")