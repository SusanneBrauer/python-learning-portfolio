# strings: Part information
part_name = "Spoiler"
print(type(part_name))

# integer: Inpection parameter
number_of_measurements = 30
print(type(number_of_measurements))

# float: Quality limits
upper_spec_limit = 0.75
print(type(upper_spec_limit))

# Boolean: Inspection result
meets_spec = True
print(type(meets_spec))

# user inputs
engineer = input("Enter engineers name:\n")
print(f"Inputs are initially {type(engineer)}")

# type conversions
measurement_result = float(input("Enter result:"))
number_of_samples = int(input("How many sample ado you have?"))

# concatonation and outputs
print("The " + part_name + " supplier provided " + str(number_of_measurements) + " samples.")
print(f"The {part_name} supplier provided {number_of_measurements} samples.")