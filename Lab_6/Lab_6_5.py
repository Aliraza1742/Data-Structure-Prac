class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None

class Stack:
    def __init__(self):
        self.top = None

    def PUSH(self, data):  # AS Stack has only one opening for entering and removing of values
        Stack_value = Node(data)
        if self.top == None:
            self.top = Stack_value
        else:
            Stack_value.pointer = self.top
            self.top = Stack_value

    def Print_stack(self):
        Top = self.top
        while Top != None:
            print(Top.data,end="")
            Top = Top.pointer

    def print_binary_equivalent(self, number):
        Input_number = number
        while Input_number != 0:
            number_modulas = Input_number % 2 # by taking modulas we are actually storin the Remainder which will be used in binary equivalent later on
            self.PUSH(number_modulas)
            Input_number = Input_number // 2
        print("The binary equivalent of : ", number, " is :",)
        self.Print_stack()

S1 = Stack()
S1.print_binary_equivalent(15)