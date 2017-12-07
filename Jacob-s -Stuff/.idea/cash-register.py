"""
Point of Sale system
Jacob Knecht & CPTR-215
2017-11-29 initial implementation of CashRegister, Inventory, and Product classes
"""

from random import randint

class CashRegister:
    def __init__(self):
        self.scanner = Scanner()
        self.inventory = Inventory()

    def process_transaction(self):
        '''
        >>> cash_register = CashRegister()
        >>> cash_register.process_transaction()
        :return:
        '''
        total = 0.0
        while True:
            id = self.scanner.scan_item()
            if id == "DONE":
                break
            product = self.inventory.product_from_id(id)
            price = product.get_price()
            tax = product.get_tax_percentage() * .01
            name = product.get_name()
            # TODO: deal with tax
            total += (price * tax) + price
            print("\t%-50s%6.2f%7.2f" % (name, price, total))
            # TODO: do something with total (and tax)
        pay_option = input('Payment Options: Cash or Card')
        if pay_option == "Card":
            CardMachine()
        else:
            CashDrawer(total, int(input('Total: %d \nEnter how much cash was recieved' % total)))

class Scanner:
    def scan_item(self):
        '''
        Scan an item:
        >>> X000S3SV1F
        '''
        return input("Scan an item: ")

class CashDrawer:
    def __init__(self, total, cash):
        '''
        >>> cash = CashDrawer(20.00, 21.00)
        Change due:  1.0
        >>> cash = CashDrawer(20.00, 25.00)
        Change due:  5.0
          $5 bills: 1
        >>> cash = CashDrawer(17.78, 20.00)
        Change due:  2.22
          $1 bills: 2
         10¢ coins: 2
          1¢ coins: 2
        '''

        # ask how much is owed
        amountOwed = total

        # ask how much was paid
        amountPaid = cash

        # display change returned
        changeOwed = amountPaid - amountOwed
        print("Change due: ", round(changeOwed, 2))

        changeOwed = int(round(changeOwed * 100))  # convert to pennies so int math works
        denominations = {2000: "$20 bills", 1000: "$10 bills",
                         500: "$5 bills", 100: "$1 bills",
                         25: "25¢ coins", 10: "10¢ coins",
                         5: "5¢ coins", 1: "1¢ coins"}
        for denomination in sorted(denominations.keys(), reverse=True):
            changeOwed = self.extractDenomination(changeOwed, denomination, denominations[denomination])

    def extractDenomination(self, amountToReturn, denominationValue, denominationLabel):
        howMany = amountToReturn // denominationValue
        amountToReturn %= denominationValue
        if howMany > 0:
            print("%10s: %d" % (denominationLabel, howMany))
        return amountToReturn


class CardMachine:
    def __init__(self):
        #I assue that the customer will always have enough money in their account
        #There are no doctests becuase the function is based on a random generated numnber
        print('Swipe Card now!')
        card = input()
        #person swipes their card
        print('Are you paying with credit or debit?')
        debit_or_credit = randint(1,2)
        if debit_or_credit == 1:
            print("Please enter your code")
            print('How much cash back would you like?')
        print('Beep boop beep beep boop')
        if debit_or_credit == 2:
            print('Please sign')
        print('Transaction Successful')
        #card machine takes card number and

class TaxCategory:
    def __init__(self, category, tax):
        self.percentage = tax
        self.category = category

    def get_percentage(self):
        return self.percentage

class Inventory:
    def __init__(self):
        nontax = TaxCategory('NonTaxable', 0.0)
        food = TaxCategory('Food and food ingredients', 4.0)
        books = TaxCategory('Everything else', 9.5)
        self.items = {"X000S3SV1F": Product("X000S3SV1F", "Bar Code Scanner", 29.99, nontax),
                      "X000M0TEN3": Product("X000M0TEN3", "Mag Stripe Reader", 9.99, nontax),
                      "MJ_tech": Product("MJ_tech", "Scanner info page", 0.00, books),
                      "4934": Product("4934", "Red Delicious Apples - Bag", 4.99, food)}

    def product_from_id(self, id):
        return self.items[id]


class Product:
    def __init__(self, id, name, price, tax_category):
        self.id = id
        self.name = name
        self.price = price
        self.tax_category = tax_category


    def get_price(self):
        return self.price

    def get_name(self):
        return self.name
    def get_tax_percentage(self):
        return self.tax_category.get_percentage()



if __name__ == "__main__":
   # import doctest
    #doctest.testmod()

    cash_register = CashRegister()
    done = False
    while not done:
        cash_register.process_transaction()
        done = input("Press Enter for another transaction, or type END: ") == "END"