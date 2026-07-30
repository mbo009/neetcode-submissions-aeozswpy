class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

class LinkedList:
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head

        while curr != None:
            if i == index:
                return curr.val
            curr = curr.nxt
            i += 1
        
        return -1
            

    def insertHead(self, val: int) -> None:
        self.head = Node(val, self.head)

    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            return

        curr = self.head
        prev = Node(-1, curr)

        while curr != None:
            prev = curr
            curr = curr.nxt

        prev.nxt = Node(val)
    
    def remove(self, index: int) -> bool:
        if index == 0:
            if self.head is not None:
                self.head = self.head.nxt
                return True
            else:
                return False
         
        curr = self.head
        prev = Node(-1, curr)
        i = 0

        while curr != None:
            if i == index:
                prev.nxt = curr.nxt
                return True

            prev = curr
            curr = curr.nxt
            i += 1

        return False

    def getValues(self) -> List[int]:
        values = []
        curr = self.head

        while curr != None:
            values.append(curr.val)
            curr = curr.nxt

        return values
        
