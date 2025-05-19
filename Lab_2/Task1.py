# For each of the following problems, give an algorithm that finds the desired numbers.
# For example, S = {6, 13, 19, 3, 8}, 19 − 3 maximizes the difference, while 8 − 6 minimizes the
# difference.
# a. Let S be an unsorted list of n integers. Write a function that takes a list as input
# and finds the pair x, y ∈ S that maximizes |x − y |.
# b. Let S be a sorted list of n integers. Write a function that takes a list as input and
# finds the pair x, y ∈ S that minimizes |x − y |.       

# a solution :

def max_value(list):
    max =list[0]
    for i in list :
        if i > max :
            max = i 
    return max 
    
def min_value(list):
    min = list [0]
    for j in list:
        if j < min :
            min = j 
    return min

def max_difference(list):
    max_num_of_list = max_value(list)
    min_num_of_list = min_value(list)
    
    max_difference =  max_num_of_list -  min_num_of_list 
    
    return (max_num_of_list , min_num_of_list)

l1 = [1,3,5,6]
print(max_difference(l1))

#  b solution :

def min_difference (list):
    first = 0
    second = 0
    result = 0 
    for i in range(len(list)):
        for j in range(len(list)) :
            if i != j :
                diff = list[i] - list[j] 
                if diff < 0 :
                   diff = -(diff)
                if result == 0:
                    result = diff
                if result > diff:
                    result = diff
                    first = list[i] 
                    second = list[j] 
                
                
    return (first,second)

l1 = [1,3,5,6]
print(min_difference(l1))