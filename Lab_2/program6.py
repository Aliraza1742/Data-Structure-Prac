# Write a recursive function to print elements of a list.

def recursive_print (list):
    if len(list) == 1 :
        print(list[0])
    else:
        print(list[0])
        return(recursive_print(list[1:]))
        
recursive_print ([1,2,3,4,5])