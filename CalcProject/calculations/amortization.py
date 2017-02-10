'''
Created on Feb 3, 2017

@author: cgregory
'''
class compute(object):
    def __init__(self):
        self.payment_num = 0
        self.interest_payment = 0
        self.principal_payment = 0
        self.balance_due = 0
        
    def __eff_int_rate(self, apr):   # effective interest per month
        eir = (apr / 100) / 12
        return eir

    def __monthly_payment(self,starting_prin, term_in_months, eir): #First Month's payment
#    mp = starting_prin * (eir / ((1 - (1 + eir)**(-1*term_in_months)))
        mp_exp = -1*term_in_months
        mp_d = (1 + eir)**mp_exp
        mp = starting_prin * (eir / (1 - mp_d))                
        return mp

    def __comp_table(self,term_in_months, starting_prin, eir, mp):
        print ("\nCompute Amortization Table\n")

        self.payment_num = range(1,term_in_months+1)
        self.interest_payment = [0] * term_in_months
        self.principal_payment = [0] * term_in_months
        self.balance_due = [0] * term_in_months

        for p in self.payment_num[:]:
            if p==1: 
                self.interest_payment[p-1] = starting_prin * eir
                self.principal_payment[p-1] = mp - self.interest_payment[p-1]
                self.balance_due[p-1] = starting_prin - self.principal_payment[p-1]
            else:
                self.interest_payment[p-1] = self.balance_due[p-2] * eir
                self.principal_payment[p-1] = mp - self.interest_payment[p-1]
                self.balance_due[p-1] = self.balance_due[p-2] - self.principal_payment[p-1]

        return 

    def __format_result(self):
        print('{0:>16s} {1:>16s} {2:>16s} {3:>16s}'.format("Payment #", "Interest", "Principal", "Balance Due"))
        payments = list(self.payment_num)

        for p in self.payment_num[:]:
            print('{0:16d} {1:16.2f} {2:16.2f} {3:16.2f}'.format(payments[p-1], self.interest_payment[p-1], self.principal_payment[p-1], self.balance_due[p-1]))
        
        return

    def calc(self,principal, apr, term_in_months): #top level loan calc
        m_eir = self.__eff_int_rate(apr)
        m_mp = self.__monthly_payment(principal, term_in_months, m_eir)
        self.__comp_table(term_in_months, principal, m_eir, m_mp)
        self.__format_result() 
        return 

