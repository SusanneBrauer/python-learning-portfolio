# spec limits
upper_spec_limit = 0.8
lower_spec_limit = -0.8

# initialise while condition
new_measurement = True

# while loop to run check till user is done
while new_measurement:
    # user enters measurement result and it get converted from string to float
    measurement = float(input("Enter your measurement result:\n"))
    # check if measurement is within spec limits (logical and-operator)
    if measurement <= upper_spec_limit and measurement >= lower_spec_limit:
        measurement_status = True
        print(f"The measurement {measurement} meets specification")
        #check if the user wants to check any other measurements
        new_entry = input("Do you want to check another measurement (y/n): ")
        if new_entry == "y":
            new_measurement = True
        else:
            new_measurement = False
    # if the enter measurement is outside of the spec
    else:
        measurement_status = False
        print(f"The measurement {measurement} does not meet the specification")
        #check if the user wants to check any other measurements
        new_entry = input("Do you want to check another measurement (y/n): ")
        if new_entry == "y":
            new_measurement = True
        else:
            new_measurement = False
            
print("Program ended")