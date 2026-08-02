def is_number(number):
    digits = str(number)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    return total == number
print (is_number(153))
print (is_number(9474))
print (is_number(123))