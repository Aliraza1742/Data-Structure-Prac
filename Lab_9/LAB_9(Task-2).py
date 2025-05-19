class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Binary_tree:
    def __init__(self):
        self.root = None

    def Insert_into_Tree(self,data):

        New_node = Node(data)


        if self.root == None:
            self.root = New_node
        else:
            list = []
            list.append(self.root)
            i=0
            while True:
                if list[i].left  == None:
                    list[i].left = New_node
                    break
                else:
                    list.append(list[i].left)
                # # if list[i].right  == None:
                # #     list[i].right = New_node
                # #     break
                # # else:
                # #     list.append(list[i].right)
                i+=1

    def Print_Breadth_first_Traverse(self):
        list = []
        list.append(self.root)

        for i in list:
            if i.left != None:
                list.append(i.left)
            if i.right != None:
                list.append(i.right)

        print("*********************** Breadth first Traversal of Binary Tree ************************ ")
        for j in list:
            print(j.data,end = " ")

B_T = Binary_tree()
B_T.Insert_into_Tree(99)
B_T.Insert_into_Tree(12)
B_T.Insert_into_Tree(56)
B_T.Insert_into_Tree(11)
B_T.Insert_into_Tree(100)
B_T.Insert_into_Tree(78)
B_T.Insert_into_Tree(89)
B_T.Insert_into_Tree(99)
B_T.Print_Breadth_first_Traverse()