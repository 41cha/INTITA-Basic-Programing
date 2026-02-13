class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            return
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = Node(value)

    def print(self):
        current_node = self.head
        joined_values = []
        while current_node != None:
            joined_values.append(str(current_node.data))
            current_node = current_node.next
        print(f"[{",".join(joined_values)}]")

    def insert(self, index, value):
        insert_node = Node(value)
        if index == 0:
            insert_node.next = self.head
            self.head = insert_node
            return
        current_node = self.head
        i = 0 
        while current_node != None and index - 1 != i:
            current_node = current_node.next
            i += 1

        if current_node == None:
            raise IndexError(f"Index {index} out of range")
        
        insert_node.next = current_node.next
        current_node.next = insert_node

if __name__ == '__main__':
    li = LinkedList()
    li.append(1)
    li.append(2)
    li.append(5)
    li.print()
    li.insert(0, 7)
    li.print()
    li.insert(2, 12)
    li.print()

