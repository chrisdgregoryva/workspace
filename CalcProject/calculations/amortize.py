'''
Created on Feb 3, 2017

@author: cgregory
'''
from calculations.amortization import compute

def main():
    principal = int(input('Please enter the amount of the loan '))
    apr = int(input('Please enter the APR Annual Percentage Rate '))
    term_in_months = int(input('What is the loan term in months '))

    # initalize object
    comp_money = compute()

    # showing initial data
        #   print ("initial values: ", comp_money.payment_num, comp_money.interest_payment, comp_money.principal_payment, comp_money.balance_due)
    
    # call "method" (function)
    comp_money.calc(principal, apr, term_in_months) 
        #   print ("initial values: ", list(comp_money.payment_num), comp_money.interest_payment, comp_money.principal_payment, comp_money.balance_due)    

if __name__ == '__main__':        
    main()    
