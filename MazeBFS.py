from Queue import CircularQueue

def isValidPos(x,y):
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE:
        if map[y][x] == '0' or map[y][x] == 'x':
            return True
    return False

def BFS():
    print("BFS : ")
    queue = CircularQueue(100)
    queue.enqueue((0,1))

    while not queue.isEmpty():
        here = queue.dequeue()
        print(f"({here[1] + 1}, {here[0] + 1})", end=' -> ')
        (x,y) = here #이따가 (y+1, x+1) 로 바꾸어서

        if (map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y - 1):
                queue.enqueue((x, y - 1))
            if isValidPos(x, y + 1):
                queue.enqueue((x, y + 1))
            if isValidPos(x - 1, y):
                queue.enqueue((x - 1, y))
            if isValidPos(x + 1, y):
                queue.enqueue((x + 1, y))
        print('현재 스택 : ', queue)
    return False


if __name__ == "__main__":
    map = [ ['1', '1', '1', '1', '1', '1'],
            ['e', '0', '0', '0', '0', '1'],
            ['1', '0', '1', '0', '1', '1'],
            ['1', '1', '1', '0', '0', 'x'],
            ['1', '1', '1', '0', '1', '1'],
            ['1', '1', '1', '1', '1', '1'] ]
    MAZE_SIZE = 6
    result = BFS()
    if result : print('--> 미로탐색 성공')
    else : print("--> 미로탐색 실패")