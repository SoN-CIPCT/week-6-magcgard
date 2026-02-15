web_users = ["catgrl", "catboi", "bookboi", "yllwflwr", "whalewatcher"]
new_users = ["catgrl", "catboi", "superbSubaru", "plantGawd", "wheresmysock"]

for user in new_users:
    if user in web_users: 
        print ("this user name is already in use. Please choose a different user name.")
    else:
        print ("This user name is available") 

cuzco = {}
cuzco["country"] = "Peru"
cuzco["population"]= 513000
cuzco["fact"]= "It was built in the shape of a jaguar"

seattle = {
    "country": "United States",
    "population": 816600,
    "fact": "named after Native American Chief Si'ahl"
}
strasbourg = {
    "country": "France", "population": 291313, "fact": "known as the Capitol of Christmas"
}
cities = {}
cities["cuzco"] = cuzco
cities ["seattle"] = seattle
cities ["strasbourg"] = strasbourg

for city_name, info in cities.items():
    print(f"city: {city_name}")
    print(f"\tcountry: {info['country']}")
    print (f"\tpopulation: {info ['population']}")
    print (f"\tfact: {info ['fact']}")
