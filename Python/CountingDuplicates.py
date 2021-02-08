#Teo Speece
#Write a function that will return the count of distinct case-insensitive alphabetic
# characters and numeric digits that occur more than once in the input string.
# The input string can be assumed to contain only alphabets (both uppercase and lowercase)
# and numeric digits.

def duplicate_count(text):
    text = text.lower()
    print(text)
    ltext = list(text)
    ltext.sort()
    print(ltext)
    counter = 1
    duplicates = 0
    if len(ltext) == 0:
        return 0
    last = ltext[0]
    for i in range(1, len(ltext)):
        current = ltext[i]
        # print(current)
        # print("current", duplicates)
        # print(last)
        if current == last:
            counter += 1
            # print("count",counter)
        else:
            last = current
            if counter > 1:
                duplicates += 1
            counter = 1
    if counter > 1:
        duplicates += 1

    print("there are this many duplicates", duplicates)
    return duplicates


