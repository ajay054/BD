# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# city_temperatures = [("London", 15), ("Mumbai", 25)]
# fahrenheit_results = [(city, celsius_to_fahrenheit(temp)) for city, temp in city_temperatures]

# print(fahrenheit_results)
# celsius_to_fahrenheit
# 2
# city_temperatures = [("London", 15), ("Mumbai", 25)]
# fahrenheit_results = [(city, (temp * 9/5) + 32) for city, temp in city_temperatures]
# print(fahrenheit_results)

input = [("London", 15), ("Mumbai", 25)]

def temp_degrees(arr):
    results = []
    for city in arr:
        far = city[1] * 9/5 + 32
        city_data = (city[0], far)
  
        results.append(city_data)

    return results
              
print(temp_degrees(input))