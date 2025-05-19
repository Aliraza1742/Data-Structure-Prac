#  Write a recursive function that computes and returns the sum of all elements of the list

def recursive_sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return (list[0] + recursive_sum(list[1:]))
        


l1 = [1,2,3,4,5]        
print(recursive_sum(l1))
