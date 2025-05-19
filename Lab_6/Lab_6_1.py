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
            print(self.top.data)

    def IS_Empty(self):
        if self.top == None:
            print("Stack IS Empty !")
        else:
            print("Stack IS not Empty !")

    def Size(self):
        if self.top == None:
            print("The Stack Is Empty and have the size of 0")
        else:
            counter = 0
            while self.top != None:
                self.top = self.top.pointer
                counter += 1
            print("The Size OF the Stack is :", counter)

    def print_stack(self):
        top = self.top
        while top != None:
            print(top.data)

            top = top.pointer


S1 = Stack()
S1.ADD_AT_START_OF_STACK(1)
S1.ADD_AT_START_OF_STACK(2)
S1.ADD_AT_START_OF_STACK(3)
S1.ADD_AT_START_OF_STACK(4)
S1.print_stack()

S1.PEEK()

S1.IS_Empty()

S1.Size()

S1.POP()
S1.print_stack()
