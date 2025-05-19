class Job:
    def __init__(self,title,id,purpose):
        self.title = title
        self.id = id
        self.purpose = purpose
        self.next = None

class Queue_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def Enqueue(self,title,id,purpose):

         New_job = Job(title,id,purpose)

         if self.head == None and self.tail == None:
             self.head = New_job
             self.tail = New_job

         else:
            self.tail.next = New_job
            self.tail = New_job
            print("Enqueued Successfully !")

    def Dequeue(self):

        if self.head == None :
            print("Linked list is Empty !")

        else:
            self.head = self.head.next
            print("Dequeued Successfully !")


    def Is_empty(self):

        if self.head == None:
            print("Linked list is Empty !")
        else:
            print("Linked list is not Empty !")

    def Size(self):
        y = self.head
        size = 0
        while y != None:
            size += 1
            y = y.next

        print("The Size of the Queue is :",size)

    def Display_Queue(self):

        y = self.head
        counter = 1
        while y != None :
            print("The title of the Job :", counter, "is :", y.title)
            counter += 1
            y = y.next

    def Search_Job(self,element):

        string = element
        self.flag = False
        y = self.head
        while y != None :
            if y.title == string :
                print("Job with Title :", string, "Exist !",)
                self.flag = True
                break
            y = y.next

        if self.flag == False :
            print("Job with Title :", string, " Does not Exist !",)



j1 = Queue_linked_list()
j1.Enqueue("PAF","123","TO DEFEND AIR OF PAKISTAN !")
j1.Enqueue("ARMY","159","TO DEFEND LAND!")
j1.Enqueue("POLICE","177","TO SERVE COMMUNTIY !")
j1.Search_Job("ARMY")
j1.Display_Queue()








