# The mode of a list of numbers is the number that occurs most frequently in the set. The
# set {4, 6, 2, 4, 3, 1} has a mode of 4. Write a function takes a list as input and returns mode
# of the list. 

def mod(list):
    perm=0
    n=0
    for i in list:
        t=0
        for j in list[1:] :
            if i==j:
                t+=1
        if t>perm:
            perm=t
            n=i
        t=0
    print(n)
list=[12,4,3,5,3,4,6,3]

mod(list)