class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.rear=None
        self.front=None

    def menu(self):
        c=0
        while c!=5:
            print("\nQueue\n1.Enqueue\n2.Dequeue\n3.Peek\n4.Display\n5.Exit")
            c=int(input("Enter your choice(Serial Number): "))
            match c:
                case 1:
                    self.Enqueue()
                case 2:
                    self.Dequeue()
                case 3:
                    self.peek()
                case 4:
                    self.display()
                case 5:
                    print("Thank You")
                    exit()
                case _:
                    print("Invalid Choice")
    def IsEmpty(self):
        return self.rear is None
    def Enqueue(self):
        n=int(input("Enter Value: "))
        node=Node(n)
        if self.IsEmpty():
            self.front=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node
        print(f"Enqueue of {n} is Successful\n")


    def Dequeue(self):

        if self.IsEmpty():
            print("\nQueue is Empty\n")
            return
        elif self.front.next is None:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next

        print("\n Dequeue Successful")
    def peek(self):
        if self.IsEmpty():
            print("Queue is Empty\n")
        else:
            print(f"The Front element is {self.front.data}")

    def display(self):
        if self.IsEmpty():
            print("Queue is Empty")
        else:
            temp=self.front
            while temp is not None:
                print(" -> ",temp.data,end="")
                temp=temp.next
            print()

queue=Queue()
queue.menu()