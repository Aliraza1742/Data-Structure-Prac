class Node:
    def __init__(self,data):
        self.data = data

class BINARY_TREE:
    def __init__(self):
        self.Nodes_list = []

    def Insert(self,data):
        New_node = Node(data)
        self.Nodes_list.append(New_node.data)
        print("Node with data :",data,"is added Successfully !")

    def left(self,data):
        if data in self.Nodes_list:
            index = self.Nodes_list.index(data)
            left_value_of_data = 2 * index + 1
            if self.Nodes_list[left_value_of_data] != None:
                print("The value at the left of the given data ",data,"is :",self.Nodes_list[left_value_of_data])
            else:
                print("Left value doesnot Exist !")

    def Right(self,data):
        if data in self.Nodes_list:
            index = self.Nodes_list.index(data) # here i am finding out the index of the data input and with the help of this index i will
            Right_value_of_data = 2 * index + 2
            if self.Nodes_list[Right_value_of_data] != None:
                print("The value at the right of the given data ",data,"is :",self.Nodes_list[Right_value_of_data])
            else:
                print(" Right value doesnot Exist !")

    def Breath_First_Traversal(self):

        if self.Nodes_list == []:
            print("Tree is Empty ! ")
        else:
            list = []
            help = 0
            list.append(self.Nodes_list[0])

            while list != []:
                P = list[0]
                left_value = 2 * help + 1
                right_value = 2 * help + 2
                if left_value < len(self.Nodes_list):
                    list.append(self.Nodes_list[left_value])
                if right_value < len(self.Nodes_list):
                    list.append(self.Nodes_list[right_value])

                list.remove(P)
                help += 1
                print(P,end = " ")

B_T = BINARY_TREE()
B_T.Insert(99)
B_T.Insert(12)
B_T.Insert(56)
B_T.Insert(11)
B_T.Insert(100)
B_T.Insert(78)
B_T.Insert(89)
B_T.Right(99)
B_T.Breath_First_Traversal()