# Write a function that takes a list as input and prints all the LEADERS in the list. 

def leaders(list):
    count=0
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            if list[j]>list[i]:
                count+=1
        if count==0:
            print(list[i],'is the leader')
        count=0
list=[1,3,2,4,6,3,7,4,2]
leaders(list)