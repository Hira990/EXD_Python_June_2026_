
def add_city(city_name):
    if city_name not in cities:
        cities.append(city_name)
        print("City added")
    else:
        print("City already pra hua")

def remove_city(city_name):
    if city_name in cities:
        cities.remove(city_name)
        print("City removed")
    else:
        print("City not found")

def list_cities(cities):
    for city in cities:
        print(city)

cities = ["Islamabad", "Rawalpindi", "Lahore", "Faisalabad"]

while True:
    choice = input("Enter choice: 1-Add, 2-Remove, 3-List  : ")
    if choice.isdigit() and int(choice) == 1:
        city_name = input("Enter city name: ")
        add_city(city_name)
    elif choice.isdigit() and int(choice) == 2:
        city_name = input("Enter city name: ")
        remove_city(city_name)
    elif choice.isdigit() and int(choice) == 3:
        list_cities(cities)
    else:
        break