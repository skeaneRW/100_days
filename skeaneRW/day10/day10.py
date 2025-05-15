class calculate:
    def __init__(self, first_term = None):
        self.first_term = first_term
        self.get_operator()
        self.get_terms()
        self.calculate()

    def get_terms(self):
        print(f"evaluating {self.first_term if self.first_term != None else 'a'} {self.operator} b")
        if self.first_term == None:
            self.first_term = int(input("what term should we use for 'a'?  "))
        self.second_term = int(input("what term shoudl we use for 'b'?  "))
        return self.first_term, self.second_term
    
    def get_operator(self):
        operator = input("what kind of calculation do you want to do? (+, -, *, /)  ")
        if operator in ['+', '-', '*', '/']:
            self.operator = operator
        else:
            print("please choose a valid operator")
            return self.get_operator()
        return self.operator
    
    def calculate(self):
        if self.operator == '+':
            result = self.first_term + self.second_term
        elif self.operator == '-':
            result = self.first_term - self.second_term
        elif self.operator == '*':
            result = self.first_term * self.second_term
        elif self.operator == '/':
            result = self.first_term / self.second_term
        print(f"{self.first_term} {self.operator} {self.second_term} = {result}")
        play_again = input(f"would you like to perform additional calculations on {result} (y/n)?  ")
     
        if play_again == 'y':
            calculate(result)
        else:
            print("thanks for doing math!")

calculate()