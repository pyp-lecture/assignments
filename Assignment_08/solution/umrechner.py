# Aus der Vorlesung

def fahrenheit_in_kelvin(temp_in_fahrenheit):
    return 5/9 * (temp_in_fahrenheit - 32) + 273.15

def celsius_in_kelvin(temp_in_celsius):
    return  temp_in_celsius + 273.15

def kelvin_in_celsius(temp_in_kelvin):
    return temp_in_kelvin - 273.15

def kelvin_in_fahrenheit(temp_in_kelvin):
    return (temp_in_kelvin - 273.15) * 9/5 + 32

def fahrenheit_in_celsius(temp_in_fahrenheit):
    return kelvin_in_celsius(fahrenheit_in_kelvin(temp_in_fahrenheit))

def celsius_in_fahrenheit(temp_in_celsius):
    return kelvin_in_fahrenheit(celsius_in_kelvin(temp_in_celsius))

t1 = 57 # Celsius
print(fahrenheit_in_celsius(kelvin_in_fahrenheit(celsius_in_kelvin(t1))))

# 57 Celsius in Fahrenheit
# 98 Celsius in Kelvin
# 120 Fahrenheit in Celsius
# 35 Fahrenheit in Kelvin
print(celsius_in_fahrenheit(57))
print(celsius_in_kelvin(98))
print(fahrenheit_in_celsius(120))
print(fahrenheit_in_kelvin(35))
