def getTip():
    print("Welcome to tip calculator; let's get tipping!")
    bill = float(input("What was the total bill? $"))
    percent = int(input("how much do you wanna tip? 10, 12, or 15 percent? "))
    party = int(input("How many people will be splitting the bill? "))
    tip_amount = bill * (percent / 100)
    total_bill = bill + tip_amount
    total_per_person = total_bill / party
    print("\n")
    print(f"Ok, you'll want to tip: ${round(tip_amount,2)}")
    print(f"that means the Total bill is gonna be: ${round(total_bill, 2)}")
    print(f"so each per person should fork over: ${round(total_per_person,2)}")
getTip()
