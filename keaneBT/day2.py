def getTip():
    bill = float(input('how much did you spend?'))
    percent =int (input('how much do you want to tip?'))
    party  =int (input('how many of your are splitting the bill?'))
    print(type(bill))
    tip_amount = bill * (percent / 100)
    print ('ok, you will want to tip: $' + str(tip_amount))
    total = bill + tip_amount
    Price_per_person = total / party
    print('and, the total is: $' + str(total) + ' if you divide it evenly each person will pay: $' + str(Price_per_person))
getTip()