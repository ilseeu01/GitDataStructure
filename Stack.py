class stack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.top = -1
    
    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e
        else: 
            print("스택이 가득 찼습니다.")

    def pop(self):
        data = self.array[self.top]
        self.array[self.top] = None
        self.top -= 1
        return data

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1

    def peek(self):
        if (self.top == -1 ):
            return None
        return self.array[self.top]

    def __str__(self):
        # string = ''
        # for _ in range(self.top + 1):
        #     string += self.pop()
        return str(self.array[:self.top+1])

    # def copy(self):
    #     newStack = stack(self.capacity)
    #     for i in range(self.top + 1):
    #         newStack.push(self.array[i])
    #     return newStack

    # def reverse(self, newStack):
    #     for c in self.array[::-1]:
    #         newStack.push(c)
    #     return newStack
    
    def copy(self):
        """현재 스택을 복사하여 반환"""
        newStack = stack(self.capacity)
        for i in range(self.top + 1):
            newStack.push(self.array[i])
        return newStack

    def reverse(self):
        """스택의 내용을 역순으로 반환"""
        newStack = stack(self.capacity)
        for i in range(self.top, -1, -1):
            newStack.push(self.array[i])
        return newStack



if __name__ == "__main__":
    # stack = stack(3)  # 용량 3인 스택 생성

    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    # stack.push(4)  # 스택이 가득 찼습니다!

    # print("peek:", stack.peek())  # 3

    # print(stack.pop())  # 3
    # print(stack.pop())  # 2
    # print(stack.pop())  # 1
    # print(stack.pop())  # 스택이 비어 있습니다!

    revstr = stack(20)
    msg = input("문자열 입력 : ")
    for c in msg:
        revstr.push(c)
    print(revstr)
