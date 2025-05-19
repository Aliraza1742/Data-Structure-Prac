class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class Double_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

        self.Input_function()  # here I am calling the function with which I will take inputs of node.

    def Add_at_end(self, data):
        New_node = Node(data)

        if self.head == None and self.tail == None:
            self.head = New_node
            self.tail = New_node
            print("Node is added Successfully !")
            self.Input_function()

        else:
            self.tail.next = New_node           # as the node we are adding at the end have the two pointers so we have to see whether next and previous are linked !
            New_node.previous = self.tail
            self.tail = New_node
            print("Node is added Successfully !")
            self.Input_function()


    def Palindrome_check(self,head ):
        head_of_D_L_L = head
        tail_of_D_L_L = self.tail

        if head_of_D_L_L == None or tail_of_D_L_L == None:
            print("Linked list is Empty !")

        while head_of_D_L_L != None and tail_of_D_L_L != None:  # here I am doing the comparison of values from the head and tail.
            if head_of_D_L_L.data == tail_of_D_L_L.data:
                head_of_D_L_L = head_of_D_L_L.next
                tail_of_D_L_L = tail_of_D_L_L.previous
            else:
                print("It is not a Palindrome !")
                return
        print("It is a Palindrome !")



    def Input_function(self):
        user_input_of_data = int(input("Enter the number of your choice except 0 :"))
        if user_input_of_data != 0:
            self.Add_at_end(user_input_of_data)
        elif user_input_of_data == 0:
            self.Palindrome_check(self.head)

D_D_L = Double_linked_list()



