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

    def Menu_list(self):
        print("******** Welcome to the Menu *******")
        print("press '1' for Add at start '2' for  remove from start '3' for Add at End ")
        print("press '4' for Remove from End '5' for add at position '6' for Remove from position ")
        print("press '7' for value before and after position '8' search_Subject")
        print("press '9' for Size '10' for Print_Subjects '11' for Exit ")

        User_input = int(input("Enter your choice ......... "))
        if User_input == 1:
            title = str(input("Enter the title of book : "))
            credit_hours = str(input("Enter the credit hours : "))
            semester = str(input("Enter the semester : "))
            instructor = str(input("Enter the name of instructor :"))

            self.add_AT_start(title, credit_hours, semester, instructor)

        elif User_input == 2:
            self.Remove_from_start()

        elif User_input == 3:

            title = str(input("Enter the title of book : "))
            credit_hours = str(input("Enter the credit hours : "))
            semester = str(input("Enter the semester : "))
            instructor = str(input("Enter the name of instructor :"))

            self.Add_at_end(title, credit_hours, semester, instructor)

        elif User_input == 4:
            self.Remove_form_End()

        elif User_input == 5:

            position = str(input("Enter the position :"))
            title = str(input("Enter the title of book : "))
            credit_hours = str(input("Enter the credit hours : "))
            semester = str(input("Enter the semester : "))
            instructor = str(input("Enter the name of instructor :"))

            self.add_before_position(position, title, credit_hours, semester, instructor)

        elif User_input == 6:

            position = str(input("Enter the position :"))
            self.Delete_Before_position(position)

        elif User_input == 7:
            position = str(input("Enter the position :"))
            self.Value_before_and_after_Position(position)

        elif User_input == 8:

            sub_name = str("Enter the title of the subject you want to search :")
            self.searchSubject(sub_name)

        elif User_input == 9:
            self.Sizee_of_linked_list()


        elif User_input == 10:
            self.print_Double_linked_list()


        elif User_input == 11:
            pass


ddl = Double_Linked_list()
ddl.Menu_list()