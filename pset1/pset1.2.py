count = 0
index = 0

while True:
    index = s.find('bob', index)
    if index >= 0:
        count += 1
        index += 1
    else:
        break

print ("Number of times bob occurs is: %d" % count)
