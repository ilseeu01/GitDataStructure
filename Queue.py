class CircularQueue:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity
    
    def enqueue(self, e): # 큐의 맨 뒤에 추가
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = e
        else:
            print("큐과 모두 찼습니다.")


    def dequeue(self): # 큐의 앞 요소 꺼내 반환
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            data = self.array[self.front]
            self.array[self.front] = None
            return data
        else:
            print("큐가 비었습니다.")

    def peek(self): # 큐의 앞 요소 삭제하지 않고 반환
        if not self.isEmpty():
            return self.array[self.front]
        else:
            print("큐가 비었습니다.")

    def size(self):
        return (self.front - self.rear + self.capacity) % self.capacity
    
    def __str__(self):
        if self.front < self.rear:
            return str(self.array[self.front + 1:self.rear + 1])
        else:
            return str(self.array[self.front + 1:self.capacity] + self.array[0:self.rear + 1])


if __name__ == "__main__":
    q = CircularQueue(8)
    for i in "ABCDEF":
        q.enqueue(i)

    print("현재 큐 : ", q)
    print("delete : ", q.dequeue())
    print("현재 큐 : ", q)
    print("delete : ", q.dequeue())
    print("현재 큐 : ", q)
    print("delete : ", q.dequeue())
    print("현재 큐 : ", q)
    q.enqueue('G')
    q.enqueue('H')
    q.enqueue('I')
    print("현재 큐 : ", q)
