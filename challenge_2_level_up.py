guest_list = [
    "Georgia",
    "Katy",
    "Louisa",
    "Sara",
    "Gemma"
]

barred_list = [
    "James",
    "Jim",
    "Paul",
    "Edward",
    "Tom"
]

def ask_name(name):
    # input("What is your name?") # put this input into the parameters area.
        
    if name in guest_list:
            print("You can enter")
    elif name in barred_list:
            print("You are barred and therefore cannot come in.")
    else:
            print("You must wait.")

ask_name(input("What is your name?"))
# ask_name("Edward")






