"""
A program that calculates the minimum fixed monthly payment needed
in order pay off a credit card balance within 12 months
"""

def payingdebtoff_inayear(balance, annual_interestrate):

    original_bal = balance
    
    def bal_mon(num_inp):
        return num_inp + num_inp*(annual_interestrate/12)
    
    bal_due = original_bal
    pay_made = 10
    while bal_due > 0:
        for loop_var in range(1,13):
            payment = pay_made
            unpaid_bal = bal_due - payment
            bal_due = bal_mon(unpaid_bal)
        pay_made += 10
    return pay_made

def main():
    """
    Function to check test cases
    """
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: "+ str(payingdebtoff_inayear(data[0],data[1])))

if __name__ == "__main__":
    main()
