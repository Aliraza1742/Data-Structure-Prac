class Node:
    def __init__(self, title, credit_hours, semester, instructor):
        self.title = title
        self.credit_hours = credit_hours
        self.semester = semester
        self.instructor = instructor
        self.prevoius = None
        self.next = None


class Double_Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_AT_start(self, title, credit_hours, semester, instructor):

        New_node = Node(title, credit_hours, semester, instructor)

        if self.head == None and self.tail == None:
            self.head = New_node
            self.tail = New_node
            print("Subject added successfully in the Doubly linked list !")

        else:
            Head = self.head
            New_node.next = Head
            Head.prevoius = New_node
            New_node.prevoius = None
            self.head = New_node
            print("Subject added successfully in the Doubly linked list !")
        return self.Menu_list()

    def Remove_from_start(self):

        if self.head == None and self.tail == None:
            print("Linked list is empty !")
        else:
            self.head = self.head.next
            self.head.next = self.head.next
            self.head.prevoius = None
            print("Subject removed successfully !")
        return self.Menu_list()

    def print_Double_linked_list(self):

        st = self.head
        while self.head != None:
            print("The title of the book is : ", self.head.title)
            print("The credit of this subject is :", self.head.credit_hours)
            print("The semester is :", self.head.semester)
            print("The instructor of the subject is :", self.head.instructor)
            self.head = self.head.next
        return self.Menu_list()

    def Add_at_end(self, title, credit_hours, semester, instructor):

        Head = self.head
        New_node = Node(title, credit_hours, semester, instructor)

        if self.head == None and self.tail == None:
            self.head = New_node
            self.tail = New_node
            print("Subject Added successfully at the End 1! ")
            print(self.head.title)
        else:

            self.tail.next = New_node
            New_node.prevoius = self.tail
            New_node.next = None
            self.tail = New_node
            print(self.head.title)
            print("Subject Added successfully at the End 2! ")
        return self.Menu_list()

    def Remove_form_End(self):

        if self.head == None and self.tail == None:
            print("Linked List is empty !")
        else:
            self.tail = self.tail.prevoius
            self.tail.next = None
            print("Subject removed Successfully from end ! ")
        return self.Menu_list()

    def Size_of_linked_list(self):
        size = 0
        y = self.head
        while y != None:
            y = y.next
            size += 1
        return size

    def Sizee_of_linked_list(self):
        size = 0
        y = self.head
        while y != None:
            y = y.next
            size += 1
        print("Size is :", size)
        return self.Menu_list()

    def add_before_position(self, position, title, credit_hours, semester, instructor):
        positi = position

        New_node = Node(title, credit_hours, semester, instructor)

        size_of_double_linked_list = self.Size_of_linked_list()

        if self.head == None and self.tail == None:
            print("Doubly linked list is empty !")


        elif positi > size_of_double_linked_list:
            print("Position doesnot exist !")


        elif positi == 1:
            self.add_AT_start(title, credit_hours, semester, instructor)

        else:
            if positi <= size_of_double_linked_list:
                counter = 1
                y = self.head
                while counter <= positi:
                    if counter == positi:
                        New_node.next = y
                        New_node.prevoius = y.prevoius
                        y.prevoius.next = New_node
                        y.prevoius = New_node
                        print("Node added successfully at the position :", positi)
                    counter += 1
                    y = y.next
        return self.Menu_list()

    def Delete_Before_position(self, position):

        positi = position
        size_of_double_linked_list = self.Size_of_linked_list()

        if self.head == None:
            print("The linked list is empty !")
        elif positi == 1:
            self.Remove_from_start()
        elif positi > size_of_double_linked_list:
            print("Position Doesnot Exist !")
        else:
            if positi <= size_of_double_linked_list:
                counter = 1
                y = self.head
                while counter <= positi:
                    if counter == positi:
                        y.prevoius.next = y.next
                        print("Node Removed form position :", positi, "successfully !")
                    y = y.next
                    counter += 1
        return self.Menu_list()

    def Value_before_and_after_Position(self, position):
        positi = position
        size_of_double_linked_list = self.Size_of_linked_list()

        if self.head == None:
            print("Linked list is empty !")

        else:
            if positi <= size_of_double_linked_list:
                counter = 1
                y = self.head
                while counter <= positi:
                    if counter == positi:
                        P = y.prevoius
                        T = y.next
                        print("The credentials of the subject at position ", positi - 1, "are :")
                        print("Title is :", P.title)
                        print("Credit Hours are :", P.credit_hours)
                        print("Semester is  :", P.semester)
                        print("Instructor of the course is :", P.instructor)

                        print("The credentials of the subject at position ", positi + 1, "are :")
                        print("Title is :", T.title)
                        print("Credit Hours are :", T.credit_hours)
                        print("Semester is  :", T.semester)
                        print("Instructor of the course is :", T.instructor)
                    y = y.next
                    counter += 1
            return self.Menu_list()

    def searchSubject(self, sub_name):
        Subject_title = sub_name
        Found = False
        if self.head == None:
            print("Linked list is empty !")

        else:
            y = self.head
            while y != None:
                if y.title == Subject_title:
                    print("Subject Exist !")
                    Found = True
                    break
                y = y.next
            if Found == False:
                print("Subject doesnot exist !")
        return self.Menu_list()