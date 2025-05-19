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

    def Print_SUBJECT_linked_list(self):
        H = self.head
        counter = 1
        while H != None:
            print("Subject", counter, "name is :", H.title)
            counter += 1
            H = H.pointer

    def remove_from_end(self):
        if self.head == None:
            print("First add Subjects")
        else:
            y = self.head
            while y.pointer.pointer != None:
                y = y.pointer
            y.pointer = None
            print("Subject removed Successfully from End  !")

    def remove_from_start(self):
        if self.head == None:
            print("Subject List is empty ! ")
        else:
            self.head = self.head.pointer

        print("Subject removed Successfully from Start !")

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
                    y = y.pointer
                    count += 1

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


S = Subject_Linked_list()
S.add_at_start(12,112,1112,221)
S.add_at_start(189,90,9087,12)
S.add_at_start(17,82,9,12)
S.add_at_end(102,90,99,'popo')
S.add_at_end(102,'ahmed',90,112)
S.add_at_end(15,'khan',99,1122)
S.Search_subject(12)
S.Print_SUBJECT_linked_list()
S.add_at_position(2,1982,'ahmed',90,112567)
S.Print_SUBJECT_linked_list()
S.remove_from_end()
S.Print_SUBJECT_linked_list()





