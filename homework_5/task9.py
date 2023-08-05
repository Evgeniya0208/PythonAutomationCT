# Implement a function called convert_temperature that converts a temperature from Celsius to Fahrenheit. The function
# should take a positional argument celsius and one keyword argument round_digits. Assume that round_digits has a default value of 2.
def convert_temperature(celsius, round_digits=2):
    return round((celsius * 1.8) + 32, round_digits)


print(convert_temperature(32))
