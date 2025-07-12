# this is the concept of tree program
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def show(self):
        print(self.data)
        if self.left :
            print(self.left)
        if self.right:
            print(self.right)
n1=Node(99)
n0=Node(3)
n2=Node(8)
n1.left=n0
n1.right=n2
n1.show()