def city_info(city_name, contry_name, population):

    full_info=city_name+' '+contry_name+' '+population
    return full_info.title()


while True:
    print("give a city name with it's origin country and its population.")
    city_name = input("city: ")
    if city_name == 'q':
        break
    country_name = input("country: ")
    if city_name == 'q':
        break
    population = str(input("population: "))
    if population=='q':
        break

    get_info=city_info(city_name, country_name, population)
    print(get_info)