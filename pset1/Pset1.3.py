s = 'abcdefghijklmnopqrstuvwxyz'

orders = []
order = ''

for i in range(len(s)):
    if s[i] <= s[i+1:]:
        order += s[i]
    else:
        orders.append(order + s[i])
        order = ''
print ("Longest substring in alabetical order is: %s" % max(orders, key = len))
