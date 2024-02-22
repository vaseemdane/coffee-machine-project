drinks = {
    "espresso": {"water": 50, "coffee": 20},
    "latte": {"water": 200, "milk": 150, "coffee": 20},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 30},
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
print("welcome to vaseem's coffee shop")
print("please check the available resources to have your drink by typing report")
while True:
    vazu=input("what would you like to have?(espresso/latte/cappuccino)")

    if vazu=='off':
        break
    elif vazu=='report':
        for ingrediant,quantity in resources.items():
            if ingrediant=='coffee':
                print(f"{ingrediant}:{quantity}g")
            else:
                print(f"{ingrediant}:{quantity}ml")
    elif vazu in drinks:
        drink_ingredients = drinks[vazu]
        shortage = False
        for ingredient, required_quantity in drink_ingredients.items():
            if ingredient in resources and resources[ingredient] < required_quantity:
                print(f"Sorry, there is not enough {ingredient}.")
                shortage = True
                break
        if not shortage:
            print(f"Enjoy your {vazu}! have nice day")
            # Deduct resources used for the drink
            for ingredient, required_quantity in drink_ingredients.items():
                resources[ingredient] -= required_quantity
    else:
        print("please choose the correct option its invalid")



