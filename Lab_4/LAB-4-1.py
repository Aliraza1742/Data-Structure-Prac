class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def Add_at_start(self,data):

        New_node = Node(data)
        if self.head == None:
            self.head = New_node
            print("Node is successfully added !")
        else:
            previous_node = self.head
            self.head = New_node
            New_node.next = previous_node
            print("Node is successfully added !")

    def Remove_from_start(self):
        if self.head == None:
            print("Linked List is Empty !")
        else:
            self.head = self.head.next
            print("Node is successfully Added !")

    def Print_linked_list(self):
        H = self.head
        while H != None:
            print(H.data,"----->",end=" ")

            H = H.next

L_L = Linked_list()
L_L.Add_at_start(12)
L_L.Add_at_start(19)
L_L.Add_at_start(20)
L_L.Add_at_start(25)
L_L.Print_linked_list()





