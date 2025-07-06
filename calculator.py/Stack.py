## creating stacks of python
class stack:
    def __init__(self):
        self.stacks=[]
    def push(self,x):
        self.stacks=[x]+self.stacks
        return self.stacks
    def pop(self):
        return self.stacks.pop(0)
        
c=stack()
c.push(60)
c.push(50)
print(c.stacks)
print(c.pop())
print(c.stacks)
