#Teo Speece
#Instructions: In this kata you will create a function that takes a list of non-negative integers and
# strings and returns a new list with the strings filtered out.

def filter_list(l):
    print(l)
    nl = []
    # loops through the list and assigns lv the current element
    for i in range(len(l)):
        lv = l[i]
        # check to see if element is an integer if it is added to new list
        if isinstance(lv, int):
            nl.append(lv)
        else:
            continue
    print(nl)
    return nl  # a new list with the strings filtered out