
#. Write a recursive function that computes the sum of all numbers from 1 to n, where n is given as parametre

def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return ( n + recursive_sum(n-1))
        
print(recursive_sum(5))