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

    def Palindrome(self,string):
        empty_string = ""
        for i in string:
            self.PUSH(i)
        top = self.top
        while top != None:
            empty_string += top.data
            top = top.pointer
        if empty_string == string:
            print("********* The given string is a Palindrome *******")
        else:
            print("********* The given string is not a Palindrome **********")



l1 = Stack()
l1.Palindrome("dad")