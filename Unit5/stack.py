class stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack .append(item) 
        print(f"{item} pushed to stack")
 
    def safe__pop(self):
        if len(self.stack) ==0:
            print("stack is empty,nothing to pop") 
            return None
        else:
            return self.stack.pop()

    def display(self):
        print("stack:",self.stack)

s=stack()
s.push(10)
s.push(20)
s.push(30) 

s.display()