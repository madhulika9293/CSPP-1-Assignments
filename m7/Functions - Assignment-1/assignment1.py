"""
A program to calculate the credit card balance after one year
if a person only pays the minimum monthly payment required
by the credit card company each month.
"""
def payingdebtoff_inayear(balance, annual_interestrate, monthly_paymentrate):
    """
    Function to calculate balance after an year
    """
    original_bal = balance
    def pay_made(num_inp):
        return num_inp*monthly_paymentrate

    def bal_mon(num_inp):
        return num_inp + num_inp*(annual_interestrate/12)

    i = 1
    bal_due = original_bal
    while i <= 12:
        payment = pay_made(bal_due)
        unpaid_bal = bal_due - payment
        bal_due = bal_mon(unpaid_bal)
        # print(round(bal_due, 2))
        i += 1
    return round(bal_due, 2)
def main():
    """
    Function to check test cases
    """
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Remaining balance: " + str(payingdebtoff_inayear(data[0], data[1], data[2])))
if __name__ == "__main__":
    main()
