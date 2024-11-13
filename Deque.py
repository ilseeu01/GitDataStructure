from Queue import CircularQueue

class CircularDeque(CircularQueue):
    def __init__(self, capacity = 10):
        super().__init__(capacity)

    def addFront(self, e):
        if not self.isFull():
            self.array[self.front] = e
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else:
            print('덱이 꽉 찼습니다.')
    
    def addRear(self, e):
        self.enqueue(e)

    def deleteFront(self):
        self.dequeue()

    def deleteRear(self):
        if not self.isEmpty():
            data = self.array[self.rear]
            self.array[self.rear] = None
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return data
        else:
            print('덱이 비었습니다.')

    def getFront(self):
        return self.peek()

    def getRear(self):
        return self.array[self.rear]


if __name__ == "__main__":
    dq = CircularDeque()

    for i in range(9):
        if i % 2 == 0:
            dq.addRear(i)
        else:
            dq.addFront(i)

    print('홀수 -> 전단, 짝수 -> 후단', dq)

    for i in range(2): dq.deleteFront()
    for i in range(3): dq.deleteRear()
    print('전단삭제 * 2, 후단삭제 * 3', dq)

    for i in range(9,14): dq.addFront(i)
    print('전단삽입 : ', dq)
