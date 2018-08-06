"""
A program to calculate the credit card balance after one year 
if a person only pays the minimum monthly payment required 
by the credit card company each month.
"""
def payingDebtOffInAYear(balance, annualInterestRate, monthlyPaymentRate):
    original_bal = balance
    
    def pay_made(x):
        return x*monthlyPaymentRate

    def bal_mon(x):
        return (x + x*(annualInterestRate/12))

    i = 1
    bal_due = original_bal
    while i<=12:
       payment = pay_made(bal_due) 
       unpaid_bal = bal_due - payment
       bal_due = bal_mon(unpaid_bal)
       # print(round(bal_due, 2))
       i += 1

    return(round(bal_due, 2))
    print(float(bal_due))
    
    

def main():
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print(payingDebtOffInAYear(data[0],data[1],data[2]))

if __name__== "__main__":
    main()

