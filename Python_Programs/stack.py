
class BoundedStack:
    def __init__(self, max_len):
        self.max_len = max_len
        self.stack = []

    def Insert_Element(self,element):
        if len(self.stack) < self.max_len:
            self.stack.append(element)
            print(f"Inserted {element} into stack: {self.stack}")
        else:
            print(f"Stack full, unable to insert {element}")
        
    def pop_Element(self):
        self.stack.pop()
        print(f"Stack after pop operation: {self.stack}")

c = BoundedStack(2)
c.Insert_Element(1)
c.Insert_Element(2)
c.Insert_Element(3)
c.Insert_Element(4)

c.pop_Element()

c.Insert_Element(4)

