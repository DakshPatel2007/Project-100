class Atm:
    def __init__(self,card_number,pin_number):
        self.card_number = card_number
        self.pin_number = pin_number

    def cashWithdrawl(self,amount):
        new_amount = 50,000 - amount
        print("You have withdrawn " + str(amount) + "You're remaining amount is " + str(new_amount)) 
   

    def balanceEnquiry(self,amount):
        amount = 50,000
        print("Your balance is " + str(amount))

def main():
        card_number = int(input("Insert card number "))
        pin_number = int(input("Insert pin number "))
        new_object = Atm(card_number,pin_number)
        print("Choose your activity ")
        print("1.Balance Enquiery  2.Cash Withdrawl")
        action = int(input("Enter your activity number "))
        if (action == 1):
           new_object.balanceEnquiry()
        elif (action == 2):
             amount = int(input("Enter the amount "))
             new_object.cashWithdrawl(amount)
        else:
            print("Enter a valid amount")

main()