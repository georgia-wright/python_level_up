# print("this is dictionaries")

# capital_cities = {
#     "England" : "London",
#     "Scotland" : "Edinburgh",
#     "Wales" : "Cardiff",
#     "Northern Ireland" : "Belfast",
#     "Ireland" : "Dublin"
# }

# print(capital_cities)

# print(capital_cities["England"])


# activity 1

animals = {
    "Lion" : "Cub",
    "Dog" : "Puppy",
    "Cat" : "Kitten",
    "Chicken" : "Chick"
}

print(animals["Cat"])

animals["Cat"] = "Kitty"

print(animals)

print(animals.keys())

print(animals.values())

print(animals.items())

print(animals.get("Dog"))

print(animals["Dog"])

print(animals.get("Dragon"))

# print(animals["Dragon"]) - gives error

print(animals.get("Dragon", "We couldn't find a baby animal for that adult animal."))


(animals.setdefault("Pig", "Piglet"))

print(animals)

animals.pop("Lion")

print(animals)










