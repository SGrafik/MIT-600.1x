balance = 3200
annualInterestRate = 0.2

monthly_interest_rate = annualInterestRate / 12.0
payment = 10
payments = 0
rem_balance = balance

while True:
    if payments == 12 and rem_balance > 0:
            payments = 0
            rem_balance = balance
            payment += 10

    elif payments == 12 and rem_balance < balance:
        print ("Lowest Payment: %d" % payment)
        break

    else:
        rem_balance -= payment
        rem_balance = rem_balance + (monthly_interest_rate * rem_balance)
        payments += 1
