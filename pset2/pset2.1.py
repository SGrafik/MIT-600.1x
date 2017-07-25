balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(12):
    month_interest_rate = annualInterestRate / 12.0
    min_month_payment = monthlyPaymentRate * balance
    month_unpaid_balance = balance - min_month_payment
    update_balance = month_unpaid_balance + month_interest_rate * month_unpaid_balance
    balance = update_balance

print ("Remaining balance: %.2f" % balance)
