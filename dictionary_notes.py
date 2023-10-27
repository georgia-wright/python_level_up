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

# print(animals["Cat"])

# animals["Cat"] = "Kitty"

# print(animals)

# print(animals.keys())

# print(animals.values())

# print(animals.items())

# print(animals.get("Dog"))

# print(animals["Dog"])

# print(animals.get("Dragon"))

# # print(animals["Dragon"]) - gives error

# print(animals.get("Dragon", "We couldn't find a baby animal for that adult animal."))


# (animals.setdefault("Pig", "Piglet"))

# print(animals)

# animals.pop("Lion")

# print(animals)

#Challenge 3

# user_search = input("What do you want to search for?    >    ").capitalize()

# print(animals.get(user_search, "We couldn't find any results."))


#Challenge 4

#use the .setdefault option

key = input("Submit an animal name").capitalize()

value = input("Submit a baby animal name").capitalize()

if key in animals:

    print(animals.get(key, "This animal does not exist"))

else:
    animals.setdefault(key, value)

print(animals)

















