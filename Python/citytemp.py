# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# city_temperatures = [("London", 15), ("Mumbai", 25)]
# fahrenheit_results = [(city, celsius_to_fahrenheit(temp)) for city, temp in city_temperatures]

# print(fahrenheit_results)
# celsius_to_fahrenheit

city_temperatures = [("London", 15), ("Mumbai", 25)]
fahrenheit_results = [(city, (temp * 9/5) + 32) for city, temp in city_temperatures]
print(fahrenheit_results)

 