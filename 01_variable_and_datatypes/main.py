# strings
part_name = "Spoiler"

# integer
number_of_measurements = 30

# float
upper_spec_limit = 0.75

# Boolean
meets_standard = True

# inputs
engineer = input("Enter engineers name:\n")

# conversions
measurement_result = float(input("Enter result:"))
number_of_samples = int(input("How many sample ado you have?"))

# concatonation
print("The " + part_name + " supplier provided " + str(number_of_measurements) + " samples.")
print(f"The {part_name} supplier provided {number_of_measurements} samples.")