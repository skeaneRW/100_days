# pizza shop question. Ask customers for their pizza order and calculate the price based on size and toppings.

def orderPizza():
    print("You gotta slice craving? You need a pizza! Let's get you sorted out.")
    base_prices = {'s': 15, 'm': 20, 'l': 25}

    def getSize():
        size = input("First things first, how hungry are ya? (answer: s m or l)? ").lower()
        if size in base_prices:
            return size
        else:
            print("Error! Invalid size selection. Please choose 's', 'm', or 'l'.")
            return getSize()
        
    def getPepperoni(size):
        pepperoni_price = {'s': 1, 'm': 2, 'l': 3}
        wants_pepperoni = input("Do you want pepperoni on that? (answer: y/n)? ").lower()
        if wants_pepperoni == 'y':
            return pepperoni_price[size]
        elif wants_pepperoni == 'n':
            return 0
        else:
            print("Hey! Are you some kinda MEAT-HEAD??? Please answer 'y' or 'n'.")
            return getPepperoni(size)
        
    def getExtraCheese(size):
        xtra_cheese_price = {'s': 1, 'm': 2, 'l': 3}
        wants_extra_cheese = input("How about some extra cheese? (answer: y/n)? ").lower()
        if wants_extra_cheese == 'y':
            return xtra_cheese_price[size]
        elif wants_extra_cheese == 'n':
            return 0
        else:
            print("Maybe you go CHEESE in your ears, buddy! Please answer 'y' or 'n'.")
            return getExtraCheese(size)
    
    size = getSize()
    return base_prices[size] + getPepperoni(size) + getExtraCheese(size)

    
    

pizza_total = orderPizza()
print(f"Your total pizza order comes to: ${pizza_total}.")
       