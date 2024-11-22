class Node:
    def __init__(self, elem, link = None):
        self.link = link
        self.data = elem

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def isFull(self):
        return False
    
    def getNode(self, pos):
        if pos < 0:
            return None
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node
    
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.data
        
    def insert(self, pos, elem):
        before = self.getNode(pos - 1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.link)
            before.link = node

    def delete(self, pos):
        before = self.getNode(pos - 1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
            elif before.link != None:
                before.link = before.link.link

if __name__ == '__main__':
    # LinkedList 객체 생성
    ll = LinkedList()

    # 초기 상태 확인
    print("Is list empty?", ll.isEmpty())  # True

    # 노드 삽입 테스트
    print("Inserting 10 at position 0")
    ll.insert(0, 10)  # 리스트: [10]
    print("Inserting 20 at position 1")
    ll.insert(1, 20)  # 리스트: [10, 20]
    print("Inserting 15 at position 1")
    ll.insert(1, 15)  # 리스트: [10, 15, 20]

    # 삽입 후 리스트 상태 출력
    print("List contents after insertions:")
    for i in range(3):  # 현재 노드 수만큼 출력
        print(f"Position {i}: {ll.getEntry(i)}")

    # 삭제 테스트
    print("Deleting node at position 1")
    ll.delete(1)  # 리스트: [10, 20]
    
    # 삭제 후 리스트 상태 출력
    print("List contents after deletion:")
    for i in range(2):  # 현재 노드 수만큼 출력
        print(f"Position {i}: {ll.getEntry(i)}")

    # 추가 테스트
    print("Inserting 30 at position 1")
    ll.insert(1, 30)  # 리스트: [10, 30, 20]
    print("Inserting 5 at position 0")
    ll.insert(0, 5)  # 리스트: [5, 10, 30, 20]

    # 최종 리스트 상태 출력
    print("Final list contents:")
    pos = 0
    while True:
        entry = ll.getEntry(pos)
        if entry is None:
            break
        print(f"Position {pos}: {entry}")
        pos += 1
