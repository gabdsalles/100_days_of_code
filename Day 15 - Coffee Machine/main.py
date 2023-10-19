from data import resources, MENU

def choose_action(choice):

    """Direciona o programa a partir da escolha do usuário, se é um report ou um pedido."""

    if choice == "report":
        generate_report()

    elif choice in ['espresso', 'latte', 'cappuccino']:
        if is_resources_sufficient(choice):
            ask_money(choice)


def generate_report():

    """Imprime a quantidade de cada ingrediente e o lucro da máquina."""
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: ${resources['money']}")

def is_resources_sufficient(product):

    """Calcula se a máquina possui recursos para realizar tal pedido. Retorna True ou False"""
    has_resources = True
    
    ingredients_list = ['water', 'milk', 'coffee']
    if product == "espresso":
        ingredients_list.pop(1)

    for ingredient in ingredients_list:
        quantity_necessary = MENU[product]['ingredients'][ingredient]
        quantity_resource = resources[ingredient]

        if quantity_resource < quantity_necessary:
            print(f"Sorry, there is not enough {ingredient}")
            has_resources = False
            return has_resources
        
    return has_resources

def ask_money(product):
    """Pega do usuário dinheiro, calcula o troco e faz o café."""
    print("Please insert coins.")
    
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))

    cost = MENU[product]['cost']

    money_given = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)

    if money_given < cost:
        print("Sorry, that's not enough money. Money refunded")
    else:
        change = money_given - cost
        print(f'Here is your ${change} change.')
        resources['money'] += cost
        deduct_resources(product)
        print(f"Here is your {product} ☕️. Enjoy!")

def deduct_resources(product):

    """Se o café foi feito com sucesso, subtrai a quantidade de ingredientes utilizada naquele pedido."""
    ingredients_list = ['water', 'milk', 'coffee']
    if product == "espresso":
        ingredients_list.pop(1)

    for ingredient in ingredients_list:
        resources[ingredient] -= MENU[product]['ingredients'][ingredient]


choice = "teste"

while (choice != "off"):

    choice = input("What would you like? (espresso/latte/cappuccino): ")
    choose_action(choice)
