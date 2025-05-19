# Write a recursive function to print elements of a list in reverse order

def recursive_reverse_print (list):
    if len(list) == 1 :
        print(list[0])
    else:
        print(list[-1])
        return(recursive_reverse_print(list[:-1]))
        
recursive_reverse_print ([1,2,3,4,5])
