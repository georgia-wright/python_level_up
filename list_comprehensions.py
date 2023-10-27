dinosaurs = [
    "Triceratops",
    "Velociraptor",
    "Anklyosaurus",
    "Archaeopteryx",
    "Tyrannosaurus Rex",
    "Stegosaurus",
    "Iguanodon"
]


dinosaurs_2 = [

]

for i in dinosaurs:
    if "saurus" in i:
        dinosaurs_2.append(i)

print(dinosaurs_2)
        # dinosaurs_2.append()


saurus_dinosaurs = [dino for dino in dinosaurs if "saurus" in dino]

print(saurus_dinosaurs)

coffee_order = (
    "Alex - Cortado",
    "Ben - Latte",
    "Charlie - Mocha"
)
    
print(coffee_order)

coffee_order.append("Diane - Hot Chocolate")

