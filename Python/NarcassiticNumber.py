#Teo Speece
#Instructions: Your code must return true or false depending upon
#  whether the given number is a Narcissistic number in base 10.
#A Narcissistic Number is a positive number which is the sum of its
#  own digits, each raised to the power of the number of digits in a given base.
# In this Kata, we will restrict ourselves to decimal (base 10).

def narcissistic(value):
    # splitting value integer into multiple integers found on
    # https://stackoverflow.com/questions/1906717/splitting-integer-in-python
    vlist = list(map(int, ' '.join(str(value)).split()))
    print(vlist)
    acc = 0
    for i in range(len(vlist)):
        num = vlist[i]
        numnar = num ** (len(vlist))
        acc += numnar
    print(acc)
    if value == acc:
        return True
    else:
        return False
