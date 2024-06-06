def convert_c_to_f(temp_in_celsius):
    temp_in_fahrenheit = temp_in_celsius + 1.8 + 32
    return temp_in_fahrenheit

temperature_in_fahrenheit = convert_c_to_f(20)
print(temperature_in_fahrenheit)
