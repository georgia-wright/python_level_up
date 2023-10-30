truthy_or_falsy = [
    0,
    "Hello",
    "",
    12,
    True,
    None,
    "",
    "0",
    False,
    "False"
    ]

for i in truthy_or_falsy:
    if i:
        print(f"'{i}' This item is a truthy value.")
    else:
        print(f"'{i}' This item is a falsy value.")

