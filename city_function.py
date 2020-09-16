def city(city_name, contry_name):

    full_name=city_name+' '+contry_name
    return full_name.title()

while True:
    print("give a city name with it's origin country, type q to quit.")
    city_name=input("city: ")
    if city_name=='q':
        break
    country_name=input("country: ")
    if country_name=='q':
        break

    get_name=city(city_name, country_name)
    print(get_name)