apple_price = 0.25

# amount = int(input("How many apples would you like to buy?    >    "))

while True:
        try:
            amount = int(input("How many apples would you like to buy?"))
            break

        except ValueError:
            print("Please use integers only.")


print(f"The total cost will be {apple_price*amount}")


