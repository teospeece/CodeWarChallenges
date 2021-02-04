#Teo Speece
#Your task is to write a function that takes a string and return a new string with all vowels removed.

def disemvowel(string):
    print(string) #prints string input
    vowels = ["a","e","i","o","u","A","E","I","O","U"] #vowels upper and lowercase
    #loops through the string to remove vowels
    for i in string:
        if i in vowels:
            string = string.replace(i,"")
    print(string)
    return string