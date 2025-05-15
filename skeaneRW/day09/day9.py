class Silent_Auction:
    def __init__(self):
        self.bids = []
        self.bid_closed = False
        self.add_bidder()

    def add_bidder(self):
        name = input("what's the bidders name?  ")
        amt = int(input("how much is the bid?   "))
        self.bids.append({"name": name, "total": amt })
        self.add_additional()

    def add_additional(self):
        while not self.bid_closed:
            add_another = input('add another bidder? (y/n)   ')
            if add_another.lower() == 'y':
                self.add_bidder()
            elif add_another != 'n':
                print("please answer 'y' or 'n' only.")
            else:
                self.bid_closed = True
                self.get_winner()

    def get_winner(self):
        highest_bidder = self.bids[0]
        for bid in self.bids:
            if bid['total'] > highest_bidder['total']:
                highest_bidder = bid
        print(f"The winner is {highest_bidder['name']} with a bid of ${highest_bidder['total']}.")
            

Silent_Auction()