class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None


class Stack:
    def __init__(self):
        self.top = None

    def ADD_AT_START_OF_STACK(self, data):  # AS Stack has only one opening for entering and removing of values
        Stack_value = Node(data)
        if self.top == None:
            self.top = Stack_value
        else:
            Stack_value.pointer = self.top
            self.top = Stack_value

    def POP(self):
        if self.top == None:
            print("STACK IS EMPTY !")
        else:
            self.top = self.top.pointer

    def PEEK(self):
        if self.top == None:
            print("STACK IS EMPTY !")
        else:
            print("The element at the top of the stack is : ")
            return self.top.data

    def print_stack(self):
        top = self.top
        print("The Stack is :")
        while top != None:
            print(top.data)
            top = top.pointer


class Linked_list:
    def __init__(self):
        self.top = None

    def ADD_AT_start(self, Node):
        Head = self.top
        if self.top == None:
            self.top = Node
        else:
            Node.pointer = self.top
            self.top = Node
            print("Added Successfully !")

    def Reverse_linked_list(self):
        Stack_element = Stack.PEEK(self)
        print(Stack_element)

    def print_linked_list(self):
        y = self.head
        while y != None:
            print("Element is :", y)
            y = y.pointer


S1 = Stack()
S1.ADD_AT_START_OF_STACK(1)
S1.ADD_AT_START_OF_STACK(2)
S1.ADD_AT_START_OF_STACK(3)
S1.ADD_AT_START_OF_STACK(4)

print(S1.PEEK())






