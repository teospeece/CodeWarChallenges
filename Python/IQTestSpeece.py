#Teo Speece
#Instructions: find out which one of the given numbers differs from the others. test by using evenness

def iq_test(numbers):
    #print(numbers)
    numbers = numbers.split(" ")
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    print(numbers)
    even = []
    odd = []
    for i in range(len(numbers)):
        num = numbers[i]
        #print(num)
        if numbers[i]%2 == 0:
            even.append(num)
        else:
            odd.append(num)
    if len(odd) < len(even):
        unlike = odd[0]
    else:
        unlike = even[0]
    for i in range(len(numbers)):
        num = numbers[i]
        if num == unlike:
            ans = i
    return ans + 1