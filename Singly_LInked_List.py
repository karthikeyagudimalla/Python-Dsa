class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def menu(self):
        c=0
        while c!=9:
            print("\nLinked List\n1.Create at beginning\n2.Create at end\n3.Create at a position\n4.Delete at beginning\n5.Delete at End\n6.Delete at position\n7.Update value\n8.display\n9.Exit\n")
            c=int(input("Enter your choice(serial number): "))
            match c:
                case 1:
                    self.create_at_beginning()
                case 2:
                    self.create_at_end()
                case 3:
                    self.create_at_position()
                case 4:
                    self.del_at_beginning()
                case 5:
                    self.del_at_end()
                case 6:
                    self.del_at_pos()
                case 7:
                    self.update_value()
                case 8:
                    self.display()
                case 9:
                    print("Thank You")
                    exit()
                case _:
                    print("Invalid Choice")
                    
            

    def create_at_beginning(self):
        n=int(input("Enter the value: "))
        self.node=Node(n)
        if(self.head==None):
            self.head=self.node
            self.node.next=None
        else:
            temp=self.head
            self.head=self.node
            self.node.next=temp
        print(n," inserted at beginning successfully")

    def create_at_end(self):
        n=int(input("Enter the value: "))
        self.node=Node(n)
        if(self.head==None):
            self.head=self.node
            self.node.next=None
        else:
            current=self.head
            while(current.next is not None):
                current=current.next
            current.next=self.node
            self.node.next=None
        print(n," inserted at end successfully")

    def create_at_position(self):
        pos=int(input("Enter the position: "))
        n=int(input("Enter the value: "))
        self.node=Node(n)
        if(self.head==None):
            self.head=self.node
            self.node.next=None
        else:
            current=self.head
            for i in range(1,pos-1):
                if(i<pos-2):
                    if(current.next==None):
                        print("Invalid position")
                        return
                current=current.next

            if(current.next==None):
                current.next=self.node
                self.node.next=None
            else:
                self.temp=current.next
                current.next=self.node
                self.node.next=self.temp
                print(f"{n} inserted at position {pos} successfully")

    def del_at_beginning(self):
        if(self.head==None):
            print("Linked List is Empty")
        else:
            self.head=self.head.next
            print("Deleted from beginning successfully")
            
    def del_at_end(self):
        if(self.head==None):
            print("Linked List is empty")
            return
        else:
            current=self.head
            while current.next.next is not None:
                current=current.next
            current.next=None
            print("Deleted from end successfully")
            
    def del_at_pos(self):
        pos=int(input("Enter the position: "))
        if(self.head==None):
            print("Linked List is empty")
            return
        elif(pos==1):
            self.del_at_beginning()
        else:
            current=self.head
            for i in range(1,pos-1):
                if(i<pos-2):
                    if(current.next==None):
                        print("Invalid Position")
                        return
                current=current.next
            current.next=current.next.next
            print(f"Deleted from position {pos} successfully")

    def update_value(self):
        if(self.head==None):
            print("Linked List is empty")
            return
        pos=int(input("Enter the position of the node: "))
        val=int(input("Enter the updated value: "))
        current=self.head
        for i in range(1,pos-1):
            if(i<pos-2):
                if(current.next==None):
                    print("Invalid position")
                    return
            current=current.next
        current.data=val
        print("Updation Successful")

  
    def display(self):
        current=self.head
        if(self.head==None):
            print("Linked List is Empty")
            return
        while current is not None:
            print(current.data,end=" -> ")
            current=current.next
        print(None)

ll=LinkedList()
ll.menu()
