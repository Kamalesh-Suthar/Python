from car import ElectricCar

my_new_ecar = ElectricCar('Audi', 'r5', 2024)
print(my_new_ecar.get_descriptive_name())
my_new_ecar.battery.describe_battery()
my_new_ecar.battery.get_range()