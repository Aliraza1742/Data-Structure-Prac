class Node:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
        self.next = None

class person_linked_list:
    def __init__(self):
        self.head = None

    def add_at_end(self,Node):
        if self.head == None:
            self.head = Node
            print("Node added Successfully !")
        else:
            y = self.head
            while y.next != self.head:
                y = y.next
            y.next = Node
            print("Node added Successfully !")

    def Remove_from_End(self):
        if self.head == None:
            print("Linked list is Empty !")
        else:
            h = self.head
            while h.next != None:
                h = h.next
            h.next = None
            print("Node is removed successfully !")

    def Display_person(self):
        N = self.head
        while N != None:
            print("Name is : ",N.name)
            print("Age is : ",N.age)
            print("City is : ",N.city)
            print("********************")
            N = N.next

Person_1 = Node("ali","18","rawalpindi")
Person_2 = Node("raza","56","rawalpindi")
Person_3 = Node("arshad","64","rawalpindi")
Person_4 = Node("bilal","20","pindi-gheb")

P_l_l = person_linked_list()
P_l_l.add_at_end(Person_1)
P_l_l.add_at_end(Person_2)
P_l_l.add_at_end(Person_3)
P_l_l.add_at_end(Person_4)
P_l_l.Display_person()
