class book:
    def __init__(self,title,author,edition):
        self.title = title
        self.author = author
        self.edition = edition
        self.pointer = None

class Book_linked_list:
    def __init__(self):
        self.head = None


    def AddatStart(self,title,author,edition):
        Head = self.head

        Node = book(title,author,edition)

        if self.head == None:
            self.head = Node
            print("**** Book Added ****")
        else:
            Node.pointer = Head
            self.head = Node
            print("**** Book Added ****")
        return self.Menu_list()


    def RemovefromStart(self):

        if self.head == None:
            print("Cannot remove books first add  the books ! ")
        else:
            self.head = self.head.pointer
            print("Book Removed Successfully !")
        return self.Menu_list()


    def add_at_end(self,title,author,edition):


        Node = book(title,author,edition)

        if self.head == None:
            self.head = Node
        else:
            Y = self.head
            while Y.pointer != None:
                Y = Y.pointer
            Y.pointer = Node
            Node.pointer = None

        print("Books are added successfully at the End !")
        return self.Menu_list()

    def RemovefromEnd(self):

        if self.head == None:
            print("Cannot remove books first add  the books ! ")
        else:
            V = self.head
            while V.pointer.pointer != None:
                V = V.pointer
            V.pointer = None
        print("Book Removed Successfully from the end ! ")
        return self.Menu_list()

    def DisplayBooks(self):
        B = self.head
        counter = 1
        while B != None :
            print("Book ",counter," Title is :",B.title)
            counter += 1
            B = B.pointer
        return self.Menu_list()


    def SearchBook(self,title):
        B = self.head
        while B != None:
            if B.title == title:
                print("Book Exist ")
                break
            B = B.pointer
        return self.Menu_list()


    def BooksCount(self):
        B = self.head
        counter = 0
        while B != None:
            counter += 1
            B = B.pointer

        print("THE Total number of books are :",counter)
        return self.Menu_list()

    def Exit(self):
        pass

    def Menu_list(self):
        print("******** Welcome to the Menu *******")
        print("press '1' for Add at start '2' for  remove from start '3' for Add at End ")
        print("press '4' for Remove from End '5' for Displaying Books '6' for Search book ")
        print("press '7' for Books Count '8' for Exit")

        User_input = int(input("Enter your choice ......... "))
        if User_input == 1:

            title_input  = str(input("Enter the title of book : "))
            author_input = str(input("Enter the name of author : "))
            edition_input = str(input("Enter the Edition number : "))
            self.AddatStart(title_input,author_input,edition_input)

        elif User_input == 2:
            self.RemovefromStart()

        elif User_input == 3:

            title_input = str(input("Enter the title of book : "))
            author_input = str(input("Enter the name of author : "))
            edition_input = str(input("Enter the Edition number : "))
            self.add_at_end(title_input, author_input, edition_input)

        elif User_input == 4:
            self.RemovefromEnd()

        elif User_input == 5:
            self.DisplayBooks()

        elif User_input == 6:
            title_input = str(input("Enter the title of book : "))
            self.SearchBook(title_input)

        elif User_input == 7:
            self.BooksCount()

        elif User_input == 8:
            self.Exit()

book1 = Book_linked_list()
book1.Menu_list()


