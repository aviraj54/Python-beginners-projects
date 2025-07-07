## creating queue in python
class queue:
    def __init__(self):
        self.queues=[]
    def enqueue(self,x):
        self.queues.append(x)
    def dequeue(self):
        font=self.queues.pop(0)
        return font
    
c=queue()
c.enqueue(40)
c.enqueue(50)
print(c.queues)
print(c.dequeue())
print(c.queues)