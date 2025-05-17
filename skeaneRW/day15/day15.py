class CoffeeMachine:
    def __init__(self):
        self.resources = self.get_starting_resources()
        self.menu = {
            "Espresso": {"Price":1.50, "Water": 50, "Coffee":18, "Milk": 0},
            "Latte": {"Price":2.50, "Water": 200, "Coffee":24, "Milk": 150},
            "Cappuccino": {"Price":3.00, "Water": 250, "Coffee":24, "Milk": 100},
        }
        self.take_order()

    def get_starting_resources(self):
        starting_resources = {
            "Water": {"unit":"ml", "unit_qty": 300},
            "Milk": {"unit":"ml", "unit_qty": 200},
            "Coffee": {"unit":"g", "unit_qty": 100},
            "Money": {"unit":"$", "unit_qty": 0},
        }
        return starting_resources
    
    def check_resources(self, menu_item):
        for key in menu_item.keys():
            if key != 'Price':
                if menu_item[key] > self.resources[key]["unit_qty"]:
                    print(f"there's not enough {key.lower()} to serve that drink.")
                    return False
        return True
    
    def collect_payment(self, price):
        print(f"you owe ${price} for this drink.\n")
        num_quarters = input("how many quarters will you insert?    ")
        num_dimes = input("how many dimes will you insert?    ")
        num_nickels = input("how many nickles will you insert?    ")
        num_pennies = input("how many quarters will you insert?    ")
        total_paid = ((int(num_quarters) * 25) + (int(num_dimes) * 10) + (int(num_nickels) * 5) + int(num_pennies))/100
        if total_paid < float(price):
            return False
        else:
            change = total_paid - float(price)
            print(f"your change is {change}") 
        return True

    def adjust_resources(self, menu_item):
        self.resources["Money"]["unit_qty"] += menu_item["Price"]
        self.resources["Water"]["unit_qty"] -= menu_item["Water"]
        self.resources["Coffee"]["unit_qty"] -= menu_item["Coffee"]
        self.resources["Milk"]["unit_qty"] -= menu_item["Milk"]
        return True
    
    def fill_drink_order(self, drink):
        def get_menu_item(drink):
            if drink == 'c':
                return self.menu["Cappuccino"]
            elif drink == 'e':
                return self.menu["Espresso"]
            else:
                return self.menu["Latte"]
        menu_item = get_menu_item(drink)
        has_resources = self.check_resources(menu_item)
        if not has_resources:
            print("sorry. we are out of stock on that item.")
        else:
            has_paid = self.collect_payment(menu_item["Price"])
            if not has_paid:
                print("this is not enough money.")
            else:
                self.adjust_resources(menu_item)
        return self.take_order()

    def print_report(self):
        for key in self.resources.keys():
            value = self.resources[key]
            print_value = str(value["unit_qty"]) + value["unit"] if key != 'Money' else value['unit'] + str(value['unit_qty'])
            print(f"{key}: {print_value}")
        return self.take_order()

    def take_order(self):
        while True:
            order = input("What would you like? (espresso = 'e'/latte = 'l'/cappuccino = 'c') ").lower()
            if order in ['e', 'l', 'c']:
                return self.fill_drink_order(order)
            elif order == 'report':
                return self.print_report()
            elif order == 'off':
                print("this machine has been turned off.")
                return
            else:
                print("please enter a valid option")

CoffeeMachine()
            
