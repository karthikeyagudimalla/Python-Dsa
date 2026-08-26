class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def menu(self):
        c=0
        while c!=10:
            print("\nDoubly Linked List\n1.Insert at beginning\n2.Insert at End\n3.Insert at position\n4.Delete at beginning\n5.Delete at End\n6.Delete at position\n7.Update Value\n8.Display from Beginning\n9.Display from End\n10.Exit\n")
            c=int(input("Enter your choice(serial number): "))
            match c:
                case 1:
                    self.insert_at_beginning()
                case 2:
                    self.insert_at_end()
                case 3:
                    self.insert_at_pos()
                case 4:
                    self.del_at_beginning()
                case 5:
                    self.del_at_end()
                case 6:
                    self.del_at_pos()
                case 7:
                    self.update_at_pos()
                case 8:
                    self.display_front()
                case 9:
                    self.display_end()
                case 10:
                    print("\nThank You")
                    exit()
                case _:
                    print("invalid choice!!")

    def insert_at_beginning(self):
        n=int(input("\nEnter the value: "))
        node=Node(n)
        if self.head is None:
            self.head=node

        else:
            temp=self.head
            self.head=node
            node.next=temp
            temp.prev=node
        if self.head.next is None:
            self.tail=node
        print("\nInsertion at Beginning Successful\n")

    def insert_at_end(self):
        n=int(input("\nEnter the value: "))
        node=Node(n)
        temp=self.head
        if self.head is None:
            self.head=node
        else:
            while temp.next is not None:
                temp=temp.next
            temp.next=node
            node.prev=temp
            node.next=None
        self.tail=node
        print("\nInsertion successful at End\n")

    def insert_at_pos(self):
        pos=int(input("\nEnter position: "))
        if pos<=0:
            print("Invalid Position")
            return
        n=int(input("Enter the value: "))
        node=Node(n)
        temp=self.head
        if pos==1:
            if self.head is None:
                self.head=node
            else:
                temp=self.head
                node.next=temp
                temp.prev=node
                self.head=node

        else: 
            for i in range(1,pos):
                if i<pos :
                    if temp is None :
                        print("\nInvalid Position")
                        return
                temp=temp.next
            if temp is None:  
                cur=self.head          
                while cur.next is not None:
                    cur=cur.next
                cur.next=node
                node.prev=cur
                node.next=None
            else:    
                node.prev=temp.prev
                node.next=temp
                temp.prev.next=node
                temp.prev=node
            if node.next is None:
                self.tail=node
        print(f"\nInsertion at position {pos} successful\n")

    def del_at_beginning(self):

        if self.head is None:
            print("Linked List is empty")
        else:
            if self.head.next is None:
                self.head = None
                self.tail=self.head
            else:    
                self.head=self.head.next
                self.head.prev=None
            print("\nDeleted from beginning successfully\n")

    def del_at_end(self):
        if self.head is None:
            print("Linked List is empty")
        elif self.head.next is None:
            self.head=None
            self.tail=self.head
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None
            self.tail=temp.prev
            print("\nDeleted form end Successfully\n")

    def del_at_pos(self):
        pos=int(input("\nEnter the position: "))
        if pos<=0:
            print("Invalid Position")
            return
        temp=self.head
        if temp is None:
            print("Linked List is empty")
            return
        if pos==1:
            if self.head.next is None:
                self.head=None
                self.tail=self.head
            else:
                self.head=self.head.next
                self.head.prev=None
        else:
            for  i in range(1,pos):
                if i<pos-1:
                    if temp.next is None:
                        print("Invalid Position")
                        return
                temp=temp.next
            if temp.next is None:
                temp.prev.next=None
                self.tail=temp.prev
            else:
                temp.next.prev=temp.prev
                temp.prev.next=temp.next
                
            print(f"\nDeletion at position {pos} successful\n")

    def update_at_pos(self):
        pos=int(input("\nEnter the position: "))
        if pos<=0:
            print("Invalid Position")
            return
        val=int(input("Enter Value to be updated: "))
        temp=self.head
        for i in range(1,pos):
            if i<pos-1:
                if temp.next is None:
                    print("Invalid Position")
                    return
            temp=temp.next
        temp.data=val
        print(f"\nValue updated at position {pos} successfully\n")     

    def display_front(self):
        temp=self.head
        if self.head is None:
            print("Linked List is empty")

        else:
            while temp is not None:
                print(temp.data,end=" -> ")
                temp=temp.next
            print("None")

    def display_end(self):
        if self.tail is None:
            print("Linked List is Empty")
        else:
            temp=self.tail
            print("None",end="")
            while temp is not None:
                print(" -> ",temp.data,end="")
                temp=temp.prev
            print()
            


ll=LinkedList()
ll.menu()