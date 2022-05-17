from Materials import MENU, resources
order = input("What would you like? (espresso/latte/cappuccino):")
machine_state = True

if order == "report":
    for i in resources:
        print(f"{i}: {resources[i]}")


rest_of_resources = resources
order_ingredients = MENU[order]["ingredients"]


def check_resource():
    enough = True
    for k in order_ingredients:
        if order_ingredients[k] > rest_of_resources[k]:
            print(f"Sorry, there is not enough {k}.")
            enough = False
    return enough


def process_coins():
    n_quarter = int(input("How many quarters?"))
    n_dimes = int(input("How many dimes?"))
    n_nickles = int(input("How many nickles?"))
    n_pennies = int(input("How many pennies?"))
    quarters, dimes, nickles, pennies = (0.25, 0.1, 0.05, 0.01)
    total_money = sum(n_quarter*quarters, n_dimes*dimes, n_nickles*nickles, n_pennies*pennies)
    return total_money
