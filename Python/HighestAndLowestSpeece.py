#Teo Speece
#Instructions: In this little assignment you are given a string of space separated numbers,
# and have to return the highest and lowest number.
#link: https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python


def high_and_low(numbers):
    numbers = numbers.split(" ")
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    print(numbers)
    max = numbers[0]
    min = numbers[0]
    for i in range(len(numbers)):
        num = numbers[i]
        if max < num:
            max = num
        if min > num:
            min = num
    return str(max)+" "+str(min)