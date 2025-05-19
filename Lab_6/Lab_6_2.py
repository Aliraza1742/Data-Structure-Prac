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

    def POP(self):
        if self.top == None:
            print("STACK IS EMPTY !")
        else:
            self.top = self.top.pointer

    def PEEK(self):
        if self.top == None:
            print("STACK IS EMPTY !")
            return None
        else:
            return self.top

    def bracket_check(self, bracket_set):
        for brack in bracket_set:
            if brack == '[' or brack == '(' or brack == '{':
                self.PUSH(brack)
            elif brack == ')' and S1.PEEK().data == '(':
                self.POP()
            elif brack == ']' and S1.PEEK().data == '[':
                self.POP()
            elif brack == '}' and S1.PEEK().data == '{':
                self.POP()
            else:
                print(" INVALID COMBINATION OF BRACKET ! ")

        if self.PEEK() == None:
            print("***** COMBINATIONS OF BRACKET IS VALID ******")

    def print_stack(self):
        top = self.top
        while top != None:
            print(top.data)
            top = top.pointer


S1 = Stack()
x = '[()]'
S1.bracket_check(x)
