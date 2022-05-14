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


