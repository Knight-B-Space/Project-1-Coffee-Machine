from Materials import MENU, resources


def report():
    print("Current resources are:\n")
    for i in rest_of_resources:
        print(f"{i}: {rest_of_resources[i]}")


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
    total_money = n_quarter*quarters + n_dimes*dimes + n_nickles*nickles + n_pennies*pennies
    return total_money


machine_state = True
rest_of_resources = resources
while machine_state:
    order = input("What would you like? (espresso/latte/cappuccino):")
    if order == "report":
        report()
    elif order == "off":
        machine_state = False
    else:
        order_ingredients = MENU[order]["ingredients"]
        order_cost = MENU[order]["cost"]
        resource_status = check_resource()
        if resource_status:
            insert_money = process_coins()
            if insert_money < order_cost:
                print("Sorry, that's not enough money. Money refunded")
            elif insert_money == order_cost:
                for k in MENU[order]["ingredients"]:
                    rest_of_resources[k] -= MENU[order]["ingredients"][k]
                    print(f"Here is your {order}. Enjoy!")
                    report()
            else:
                for k in MENU[order]["ingredients"]:
                    rest_of_resources[k] -= MENU[order]["ingredients"][k]
                print(f"Here is your {order}. Enjoy!\n")
                report()
                change = round(insert_money - order_cost, 2)
                print(f"Here is ${change} dollars in change")
