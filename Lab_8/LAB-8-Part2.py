class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.middle = None
class Tree:
    def __init__(self):
        self.root = None

    def Breadth_first(self, root):
        lst_of_tree_nodes = []  # this list will hold all the nodes of the tree level by level

        lst_of_tree_nodes.append(root)

        for i in lst_of_tree_nodes:
            if i != None:
                lst_of_tree_nodes.append(i.left)
                lst_of_tree_nodes.append(i.middle)
                lst_of_tree_nodes.append(i.right)

        # print(lst_of_tree_nodes)
        print("***** Breadth First order of Tree is ***** ")
        for j in lst_of_tree_nodes:
            if j != None:
                print(j.data, "----->", end = "")


def main():

    tree = Tree()
    tree.root = node (20)
    tree.root.left = node (10)
    tree.root.middle = node (1220)
    tree.root.middle.left = node (2220)
    tree.root.middle.middle = node (3220)
    tree.root.right = node (30)
    tree.root.left.left = node (100)
    tree.root.left.right = node (45)
    tree.root.right.left = node (50)
    tree.root.right.right = node (90)
    tree.root.left.left.left = node (110)
    tree.root.left.left.right = node (230)
    tree.root.left.right.left = node (105)
    tree.root.left.right.right = node (188)
    tree.root.right.left.left = node (122)
    tree.root.right.left.right = node (43)
    tree.root.right.right.left = node (55)
    tree.root.right.right.right = node (360)

    tree.Breadth_first(tree.root)

print("Breadth first traversal of tree is :")
main()