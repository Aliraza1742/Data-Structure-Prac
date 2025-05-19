class Subject:
    def __init__(self, title, credit_hours, semester, instructor):
        self.title = title
        self.credit = credit_hours
        self.semester = semester
        self.instructor = instructor
        self.pointer = None


class Subject_Linked_list:
    def __init__(self):
        self.head = None

    def add_at_start(self, title, credit_hours, semester, instructor):
        head = self.head
        New_node = Subject(title, credit_hours, semester, instructor)
        if self.head == None:
            self.head = New_node
        else:
            New_node.pointer = self.head
            self.head = New_node
        print("Subjects are Added ! ")
        self.Menu_list()

    def Print_SUBJECT_linked_list(self):
        H = self.head
        counter = 1
        while H != None:
            print("Subject", counter, "name is :", H.title)
            counter += 1
            H = H.pointer
        self.Menu_list()

    def remove_from_end(self):
        if self.head == None:
            print("First add Subjects")
        else:
            y = self.head
            while y.pointer.pointer != None:
                y = y.pointer
            y.pointer = None
            print("Subject removed Successfully from End  !")
        self.Menu_list()

    def remove_from_start(self):
        if self.head == None:
            print("Subject List is empty ! ")
        else:
            self.head = self.head.pointer

        print("Subject removed Successfully from Start !")
        self.Menu_list()

    def add_at_end(self, title, credit_hours, semester, instructor):

        head = self.head
        New_node = Subject(title, credit_hours, semester, instructor)

        if self.head == None:
            self.head = New_node
        else:
            u = self.head
            while u.pointer != None:
                u = u.pointer

            u.pointer = New_node
            New_node.pointer = None
        print("Subject added successfully at the End !")
        self.Menu_list()

    def size_of_list(self):
        a = self.head
        counter = 1
        while a.pointer != None:
            counter += 1
            a = a.pointer
        return counter

    def add_at_position(self, posti, title, credit_hours, semester, instructor):

        position = posti
        size = self.size_of_list()
        New_node = Subject(title, credit_hours, semester, instructor)

        if self.head == None:
            self.add_at_start()
        else:
            if position <= size:    # here i compairing the position with size just to make insure that the user enter the correct position
                count = 1
                while count + 1 <= position:
                    y = self.head
                    if count + 1 == position:
                        t = y.pointer
                        y.pointer = New_node
                        New_node.pointer = t
                        print("Added Successfully !")
                    y = y.pointer
                    count += 1
            else:
                print("Cannot add at position :",position,"as it exceeds the size of linked list .")
        self.Menu_list()

    def Remove_from_Position(self, posti):
        position = posti
        Size_of_linked_list = self.size_of_list()

        if self.head == None:
            print("Linked list is empty !")
        elif position == 1:
            self.remove_from_start()
        else:
            if position <= Size_of_linked_list:
                count = 1
                P = self.head
                while count + 1 <= position:
                    if count + 1 == position:
                        P.pointer = P.pointer.pointer
                        print("**** Node Removed Successfully ! ****")

                    P = P.pointer
                    count += 1
        self.Menu_list()

    def Value_at_Position(self, posti):
        position = posti
        Size_of_linked_list = self.size_of_list()

        if self.head == None:
            print("Linked list is Empty !")
        elif position == 1:
            print("The name of Subject at the position 1 is :", self.head.title)
        else:
            if position <= Size_of_linked_list:
                count = 1
                Y = self.head
                while count <= position:
                    if count == position:
                        print("The name of Subject at the position", position, "is :")
                        print(Y.title)

                    Y = Y.pointer
                    count += 1
        self.Menu_list()

    def Search_subject(self, name_input):
        Search_subject_name = name_input
        Found = False
        if self.head == None:
            print("The Subject List is Empty !")
        else:
            Y = self.head
            while Y != None:
                Book_Title = Y.title
                if Book_Title == Search_subject_name:
                    print("Book Exist !!")
                    Found = True
                    break

                Y = Y.pointer
            if Found == False:
                print("Book with Title :", Search_subject_name, "doesnot Exist !")
        self.Menu_list()

    def Menu_list(self):
        print("Press 1 for 'Add at end' , 2 for 'Add at start' , 3 for 'Remove from start' , 4 for 'Remove from end' " 
              "\n Press 5 for 'Add at position ' 6 for 'Remove from position ' 7 for 'Search subject', 8 for 'Value at position'"
              "\n Press 9 for 'Size of a Linked List' 10 for 'Print Linked List' 11 for 'Terminating' ")

        User_choice = int(input("Enter your choice : "))

        if User_choice == 1:

            title_input = input("Enter the title of the Subject :")
            credit_hours = input("Enter the Credit hours of subject :")
            Semester_input = input("Enter the Semester :")
            instructor_input = input("Enter the instructor name : ")

            self.add_at_end(title_input,credit_hours,Semester_input,instructor_input)

        elif User_choice == 2:

            title_input = input("Enter the title of the Subject :")
            credit_hours = input("Enter the Credit hours of subject :")
            Semester_input = input("Enter the Semester :")
            instructor_input = input("Enter the instructor name : ")

            self.add_at_start(title_input, credit_hours, Semester_input, instructor_input)

        elif User_choice == 3:
            self.remove_from_start()

        elif User_choice == 4:
            self.remove_from_end()

        elif User_choice == 5:

            position_input = int(input("Enter the positon where you want to enter the subject : "))
            title_input = input("Enter the title of the Subject : ")
            credit_hours = input("Enter the Credit hours of subject : ")
            Semester_input = input("Enter the Semester : ")
            instructor_input = input("Enter the instructor name : ")

            self.add_at_position(position_input, title_input, credit_hours, Semester_input, instructor_input)

        elif User_choice == 6:

            position_input = int(input("Enter the position from where you want to delete the subject : "))
            self.Remove_from_Position(position_input)

        elif User_choice == 7:

            title_input = input("Enter the title of the Subject you want to search  : ")
            self.Search_subject(title)

        elif User_choice == 8:

            position_input = int(input("Enter the position at which you want to know the value : "))
            self.Value_at_Position(position_input)

        elif User_choice == 9:
            print(self.size_of_list())

        elif User_choice == 10:
            self.Print_SUBJECT_linked_list()

        elif User_choice == None:
            pass

S_L_L = Subject_Linked_list()
S_L_L.Menu_list()