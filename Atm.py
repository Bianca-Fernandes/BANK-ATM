class Atm:
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number            

    def CashWithdrawl(self, amount):
        a = 50000 - amount
        print("You have withdrawn amount " + str(amount) + ". Your remaining balance is " + str(a))
    
    def CheckBalance(self):
        print("Your balance is 50000")

def main():
    card_number = input("Enter your card number: ")
    pin_number = input("Enter your pin number: ")
    user = Atm(card_number, pin_number)
    print("Choose your activity: ")
    print("1.balance enquire")
    print("2.withdrawl")
    activity = int(input("Enter activity number: "))
    if(activity == 1):
        user.CheckBalance()
    elif(activity == 2):
        amount = int(input("Enter the amount: "))
        user.CashWithdrawl(amount)
    else:
        print("Enter a valid pin number: ")

if __name__ == "__main__": 
    main()