calculation_to_seconds = 24 * 60 * 60
name_of_unit = 'minutes'

def days_to_units(number_of_days):
    print(f"{number_of_days} days are {number_of_days * calculation_to_seconds} {name_of_unit}")
    print("All good!")

print("20 days are " + str(24 * calculation_to_seconds) + " minutes")

days_to_units(15)