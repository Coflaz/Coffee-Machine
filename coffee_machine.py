import time
import os

Coffee_Machine = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
    "on": True,
}

Coffees ={
    "espresso": {
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "money": 1.5,
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "money": 2.5,
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "money": 3.0,
    },
}

def display_machine_state():
    if Coffee_Machine["on"]:
        print("\nThe coffee machine has:\n")
        print("{}ml of water".format(Coffee_Machine["water"]))
        time.sleep(0.5)
        print("{}ml of milk".format(Coffee_Machine["milk"]))
        time.sleep(0.5)
        print("{}g of coffee beans".format(Coffee_Machine["coffee"]))
        time.sleep(0.5)
        print("${}\n".format(Coffee_Machine["money"]))
        time.sleep(1.5)
    else:
        print("\nThe coffee machine is off.\n")
        time.sleep(5)

def turn_on():
    Coffee_Machine["on"] = True
    print("\nTurning on the coffee machine...\n")
    time.sleep(1.5)
    print("The coffee machine is now on.\n")
    time.sleep(5)

def turn_off():
    Coffee_Machine["on"] = False
    print("\nTurning off the coffee machine...\n")
    time.sleep(1.5)
    print("The coffee machine is now off.\n")
    time.sleep(5)

def refill_machine():
    if not Coffee_Machine["on"]:
        Coffee_Machine["water"] = 300
        Coffee_Machine["milk"] = 200
        Coffee_Machine["coffee"] = 100
        print("\nRefilling the coffee machine...\n")
        time.sleep(1.5)
        print("The coffee machine has been refilled.\n")
        time.sleep(5)
    else:
        print("\nYou can't refill the coffee machine while it's on.\n")
        time.sleep(5)

def buy_coffee():
    if not Coffee_Machine["on"]:
        print("\nThe coffee machine is off.\n")
        print("Can't buy coffee while the coffee machine is off.\n")
        time.sleep(5)
        return
    else:

        print("\nEspresso => {}ml of water, {}g of coffee beans, ${}".format(Coffees["espresso"]["water"], Coffees["espresso"]["coffee"], Coffees["espresso"]["money"]))
        time.sleep(0.5)
        print("Latte => {}ml of water, {}ml of milk, {}g of coffee beans, ${}".format(Coffees["latte"]["water"], Coffees["latte"]["milk"], Coffees["latte"]["coffee"], Coffees["latte"]["money"]))
        time.sleep(0.5)
        print("Cappuccino => {}ml of water, {}ml of milk, {}g of coffee beans, ${}\n".format(Coffees["cappuccino"]["water"], Coffees["cappuccino"]["milk"], Coffees["cappuccino"]["coffee"], Coffees["cappuccino"]["money"]))
        time.sleep(1.5)
        choice = input("\nWhat kind of coffee would you like? (espresso/latte/cappuccino) ").lower().strip()

        if (Coffees[choice]["water"] > Coffee_Machine["water"]):
            print("\nSorry, there is not enough water.\n")
            time.sleep(3)
        elif (Coffees[choice]["milk"] > Coffee_Machine["milk"]):
            print("\nSorry, there is not enough milk.\n")
            time.sleep(3)
        elif (Coffees[choice]["coffee"] > Coffee_Machine["coffee"]):
            print("\nSorry, there is not enough coffee.\n")
            time.sleep(3)
        else:
            print("\nThat will be ${}".format(Coffees[choice]["money"]))
            time.sleep(1.5)

            if input("Confirm purchase? (y/n) ").lower().strip() == "y":
                money_taken = 0

                pennies = int(input("How many pennies($0,01) did you give? "))
                nickels = int(input("How many nickels($0,05) did you give? "))
                dimes = int(input("How many dimes($0,10) did you give? "))
                quarters = int(input("How many quarters($0,25) did you give? "))

                money_taken += (pennies + (nickels * 5) + (dimes * 10) + (quarters * 25)) / 100

                if money_taken < Coffees[choice]["money"]:
                    print("\nSorry, that's not enough money. Money refunded.")
                elif money_taken > Coffees[choice]["money"]:
                    print("\nHere is ${} in change.".format(round(money_taken - Coffees[choice]["money"],2)))
                    Coffee_Machine["money"] += Coffees[choice]["money"]
                    Coffee_Machine["water"] -= Coffees[choice]["water"]
                    Coffee_Machine["milk"] -= Coffees[choice]["milk"]
                    Coffee_Machine["coffee"] -= Coffees[choice]["coffee"]
                    print("Here is your {} ☕️\n".format(choice))
                    print("Enjoy!\n")
                else:
                    Coffee_Machine["money"] += Coffees[choice]["money"]
                    Coffee_Machine["water"] -= Coffees[choice]["water"]
                    Coffee_Machine["milk"] -= Coffees[choice]["milk"]
                    Coffee_Machine["coffee"] -= Coffees[choice]["coffee"]
                    print("Here is your {} ☕️\n".format(choice))
                    print("Enjoy!\n")

            time.sleep(5)

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        display_machine_state()
        choice = input("What would you like to do? (buy/fill/turn on/turn off/exit) ").lower().strip()
        if choice == "buy":
            buy_coffee()
        elif choice == "fill":
            refill_machine()
        elif choice == "turn on":
            turn_on()
        elif choice == "turn off":
            turn_off()
        elif choice == "exit":
            print("\nGoodbye!\n")
            break
        else:
            print("\nSorry, I didn't understand that.\n")

if __name__ == "__main__":
    main()

