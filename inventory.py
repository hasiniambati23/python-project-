import json

# Load inventory
with open("inventory.json", "r") as file:
    inventory = json.load(file)

def show_inventory():
    for item, details in inventory.items():
        print(item, details)

def add_product(name, price, quantity):
    inventory[name] = {"price": price, "quantity": quantity}

def update_stock(name, quantity):
    if name in inventory:
        inventory[name]["quantity"] += quantity

def save_inventory():
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

# Menu
while True:
    print("\n1.Show Inventory  2.Add Product  3.Update Stock  4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        show_inventory()
    elif choice == "2":
        name = input("Product name: ")
        price = int(input("Price: "))
        quantity = int(input("Quantity: "))
        add_product(name, price, quantity)
        save_inventory()
    elif choice == "3":
        name = input("Product name: ")
        quantity = int(input("Add quantity: "))
        update_stock(name, quantity)
        save_inventory()
    elif choice == "4":
        break
