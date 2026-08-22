class Stack:
    def __init__(self):
        self.stack=[]
        ch =0
        while ch!=5:
            print("\nStack\n1.Push\n2.Pop\n3.Peek\n4.Display\n5.Exit\n")
            ch=int(input("Enter your choice(serial number): "))
            match ch:
                case 1:
                    self.push()
                    
                case 2:
                    self.pop()
                    
                case 3:
                    self.peek()
                    
                case 4:
                    self.display()
                    
                case 5:
                    print("Thank You")
                    exit()
        
    def push(self):
        self.value=int(input("Enter the value to push: "))
        self.stack.append(self.value)
        print(f"Pushed {self.value} successfully")
    def pop(self):
        self.popped_element=self.stack.pop()
        print(f"Popped {self.popped_element} successfully")
    def peek(self):
        print(f"top element is {self.stack[len(self.stack)-1]}")
    def display(self):
        print("The Stack is: ")
        for i in self.stack:
            print(i,end=" ")
        
s=Stack()
    