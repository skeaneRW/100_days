# sell tickets for a roller coaster- deny anyone too short, charge different prices based on age, and offer a photo for an extra charge
def sellTickets():
    print("yo yo yo, it's time to rollercoaster! ")
    height = float(input("Hey, how tall are you anyway? (in inches... no metric nonsense, please! "))
    flavor_text = ""
    if height < 38:
        print("sorry short-stuff, you're too little to go on this 'coaster!")
        return
    else:
        age = int(input("How old are you? "))
        if age < 12:
            ticket_price = 5
            flavor_text = "ok, little buddy, "
        elif age < 18:
            ticket_price = 7
            flavor_text = "I hate to let screen-agers on the ride, but "
        else:
            ticket_price = 12
            flavor_text = "You absolute Geezer! Don't you have anything better to do? If you insist, "
    wants_photo = input("You look like a sucker for a good roller-coaster photo. How about it? (answer: y/n)?").lower()
    def photo_price(yes_no):
        if yes_no == "y":
            return 3
        elif yes_no == "n":
            return 0
        else:
            yes_no = input("error! error! your response does not compute. Answer 'y' or 'n', wiseguy.").lower()
            return photo_price(yes_no)
    
    ticket_price += photo_price(wants_photo)
    print(f"{flavor_text} your ticket price is ${ticket_price}.")

sellTickets()