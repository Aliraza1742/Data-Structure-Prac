# Write a recursive function that finds and returns the minimum element from a list.

def recursive_minimum(list):
    if len(list) == 1:
        return (list[0])
    else:
        if list[0] < recursive_minimum(list[1:]):
            return list[0]
        return(recursive_minimum(list[1:]))
        

l1 = [2,3,4,1,45]
print(recursive_minimum(l1))
        