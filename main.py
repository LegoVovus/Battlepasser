import time

print("Battlepasser by legovovus")

while True:  
    print("Menu: \n 1. Start \n 2. Info \n 0. Quit")
    choice = input()
    
    if choice == "1":
        while True:
            print("Start Menu")
            print("1. Autotrade \n 2. Gambler \n 3. Cloud9 \n ... \n 0. Back")
            start_choice = input()

            if start_choice == "1":
                pass
            elif start_choice == "2":
                pass
            elif start_choice == "3":
                pass
            else: 
                print("Error! Try again")

    elif choice == "2":
        print("--- Battlepasser Info ---")
        print("Battlepasser is a script for Rugplay forks with auto- modules in it. It is to full complete battlepass on forks or just automate most of casual things. \n Github link: https://github.com/LegoVovus/Battlepasser \n")
        time.sleep(1)
    elif choice == "0":
        quit