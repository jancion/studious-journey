'''
Cash Register .01
Julian Ancion & CPTR 215
Created: 2017-08-21
Modified: 2017-08-25
'''
import math

def extract_denomination(return_amount, value, label):
    how_many = return_amount // value
    return_amount %= value
    if how_many > 0:
        print("%10s: $d" % (label, how_many))
        return return_amount




def main():
    # input information from user
    cash_owed = float(input("How much is owed? "))
    tax_type = str(input("Is this a none prepared food item? y/n "))

    yes_list = ["yes", "Yes", "y"]

    if tax_type in yes_list:
        tax = 1.055
    else:
        tax = 1.07

    cash_owed = cash_owed * tax
    print('Total Due: %.2f' % (cash_owed))
    cash_paid = float(input("How much was paid? "))


    # Calculate payment and return change

    change_owed = cash_paid - cash_owed
    print("Change Due: %.2f" % (change_owed))
    change_owed = float('%.2f' % (change_owed))
    # breakdown into bills and coins
    bills_owed = int(change_owed)
    coins_owed = int((change_owed - bills_owed) * 100)

    '''
    # change in bills
    change20 = bills_owed // 20
    bills_owed %= 20
    change10 = bills_owed // 10
    bills_owed %= 10
    change5 = bills_owed // 5
    bills_owed %= 5
    change1 = bills_owed // 1
    bills_owed %= 1
    '''
    denominations = {
        20 : "$20 bills",
        10 : "$10 bills",
        5 : "$5 bills",
        1 : "$1 bills"
    }
    for denomination in sorted(denominations.keys(), reverse = True):
        if bills_owed > 0:
            bills_owed = extract_denomination(int(bills_owed), denomination, denominations[denomination])
    ''''# change in coins
    change_quarter = coins_owed // 25
    coins_owed %= 25
    change_dime = coins_owed // 10
    coins_owed %= 10
    change_nickel = coins_owed // 5
    coins_owed %= 5
    change_penny = math.ceil(coins_owed) // 1

    if change20 > 0:
        print('Number of twenties returned is:', change20)
    if change10 > 0:
        print('Number of ten\'s returned is:', change10)
    if change5 > 0:
        print('Number of five\' returned is:', change5)
    if change1 > 0:
        print('Number of one\'s returned is:', change1)
    if change_quarter > 0:
        print('Number of quarter\'s returned is:', change_quarter)
    if change_dime > 0:
        print('Number of dime\'s returned is:', change_dime)
    if change_nickel > 0:
        print('Number of nickel\'s returned is:', change_nickel)
    if change_penny > 0:
        print('Number of penny\'s returned is:', change_penny)
    #print(change20, change10, change5, change1)
    #print(change_quarter, change_dime, change_nickel, change_penny)
    '''

main()
