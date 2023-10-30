# balance = 1000

# def cash_withdraw(amount, accnum):
#     global balance
#     print(f"You have {balance}")
    
#     balance = balance - amount
    
#     print(f"You are withdrawing {amount} from {accnum}")
#     print(f"You now have {balance}")

# cash_withdraw(20, 12345678)
# cash_withdraw(30, 12345678)


def pin_checker(user_pin):
    if user_pin == "3344":
        return True
    else:
        return False
#take user pin
#check if correct

balance = 1000

def cash_withdraw(amount,user_pin):
    global balance

    # if user_request == True:
    #     print(balance)
    # else: 

    if pin_checker(user_pin) and balance >= int(amount):
        print(f"You can withdraw {amount} from {balance}")
        balance = balance - int(amount)
        print(f"Your new balance is {balance}")
    else:
        print("You cannot withdraw money.")


def see_balance(user_request):
    global balance
    if user_request == "Yes" or user_request == "yes":
        print(balance)
    else:
        return False


# pin_checker(input("What is your pin?"))


see_balance(input("Would you like to see your balance?"))

cash_withdraw(input("Enter amount"), input("Enter pin"))








    
#if pin is correct and enough money in balance, let user withdraw cash