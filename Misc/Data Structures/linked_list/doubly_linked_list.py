class DoublyLinkedList:  # making main class named doubly linked list
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, x):
        newLink = Link(x)  # Create a new link with a value attached to it
        if self.isEmpty() == True:  # Set the first element added to be the tail
            self.tail = newLink
        else:
            self.head.previous = newLink  # newLink <-- currenthead(head)
        newLink.next = self.head  # newLink <--> currenthead(head)
        self.head = newLink  # newLink(head) <--> oldhead

    def delete_head(self):
        temp = self.head
        self.head = self.head.next  # oldHead <--> 2ndElement(head)
        self.head.previous = None  # oldHead --> 2ndElement(head) nothing pointing at it so the old head will be removed
        if self.head is None:
            self.tail = None  # if empty linked list
        return temp

    def insert_tail(self, x):
        newLink = Link(x)
        newLink.next = None  # currentTail(tail)    newLink -->
        self.tail.next = newLink  # currentTail(tail) --> newLink -->
        newLink.previous = self.tail  # currentTail(tail) <--> newLink -->
        self.tail = newLink  # oldTail <--> newLink(tail) -->

    def delete_tail(self):
        temp = self.tail
        self.tail = self.tail.previous  # 2ndLast(tail) <--> oldTail --> None
        self.tail.next = None  # 2ndlast(tail) --> None
        return temp

    def delete(self, x):
        current = self.head

        while current.value != x:  # Find the position to delete
            current = current.next

        if current == self.head:
            self.delete_head()

        elif current == self.tail:
            self.delete_tail()

        else:  # Before: 1 <--> 2(current) <--> 3
            current.previous.next = current.next  # 1 --> 3
            current.next.previous = current.previous  # 1 <--> 3

    def isEmpty(self):  # Will return True if the list is empty
        return self.head is None

    def display(self):  # Prints contents of the list
        current = self.head
        while current != None:
            current.displayLink()
            current = current.next
        print()


class Link:
    next = None  # This points to the link in front of the new link
    previous = None  # This points to the link behind the new link

    def __init__(self, x):
        self.value = x

    def displayLink(self):
        print(f"{self.value}", end=" ")
       
def main():
    D = DoublyLinkedList()
    D.insert_head(input("Inserting 1st at head ").strip())
    D.insert_head(input("Inserting 2nd at head ").strip())
    print("\nPrint list:")
    D.display()
    D.insert_tail(input("Inserting 1st at tail ").strip())
    D.insert_tail(input("Inserting 2nd at tail ").strip())
    print("\nPrint list:")
    D.display()
    
if __name__ == "__main__":
    main()
