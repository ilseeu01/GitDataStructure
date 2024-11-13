class Node:
    def __init__(self, elem, link = None):
        
        self.link = link
        self.data = elem

class LinkedStack: 
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None
    
    def isFull(self):
        return False
    
    def push(self, e):
        self.top = Node(e, self.top) #이 코드가 실행되는 시점에서 self.top = None 이다.

    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            return n.data
        
    def peek(self):
        if not self.isEmpty():
            return self.top.data
        
    def size(self):
        node = self.top
        count = 0
        while not self.isEmpty():
            node = node.link
            count += 1
        return count
    
    def __str__(self):
        arr = []
        node = self.top
        while not node == None:
            arr.append(node.data)
            node = node.link
        return str(arr)

    
if __name__ == '__main__':
    stack = LinkedStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
