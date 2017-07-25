balance = 999999
annualInterestRate = 0.18

def payment_calc(upbound, lowbound):
    """
    Supply upper and lower bounds to return the midpoint payment.
    Automatically reset the payments, up/low bounds and rem_balance for convenience.
    """
    payments = 0
    rem_balance = balance
    payment_upper = upbound
    payment_lower = lowbound
    payment = (upbound + lowbound) / 2
    return (payment, payment_upper, payment_lower, payments, rem_balance)

monthly_interest_rate = annualInterestRate / 12.0
(payment, payment_upper, payment_lower, payments, rem_balance) = payment_calc((balance * (1 + monthly_interest_rate) ** 12) / 12.0, balance / 12)

while True:
    if round(rem_balance, 2) == round(payment, 2):
        print ("Lowest Payment: %.2f" % payment)
        break

    elif payments == 12 and rem_balance > 0:
        (payment, payment_upper, payment_lower, payments, rem_balance) = payment_calc(payment_upper, payment)

    elif payments == 12 and rem_balance < 0:
        (payment, payment_upper, payment_lower, payments, rem_balance) = payment_calc(payment, payment_lower)

    else:
        rem_balance -= payment
        rem_balance = rem_balance + (monthly_interest_rate * rem_balance)
        payments += 1
