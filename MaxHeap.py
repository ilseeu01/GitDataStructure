def heappush(heap, n):
    heap.append(n)
    i = len(heap) - 1
    while i != 1:
        pi = i//2 #parent index
        if n <= heap[pi]:
            break
        heap[i] = heap[pi]
        i = pi
    heap[i] = n

def heappop(heap):
    size = len(heap) - 1
    
    if size == 0:
        return None
    
    pi = 1
    i = 2
    root = heap[1]
    last = heap[size]

    while i <= size:
        if i < size and heap[i] < heap[i+1]:
            i += 1
        if last >= heap[i]:
            break
        heap[pi] = heap[i]
        pi = i
        i *= 2

    heap[pi] = last
    heap.pop()
    return root


if __name__ == "__main__":
    # 힙 리스트 초기화 (인덱스 0은 사용하지 않으므로 None으로 채움)
    heap = [None]

    # 테스트할 입력 값 리스트
    test_values = [20, 15, 30, 5, 10, 40, 25]

    # 값 삽입 테스트 (heappush)
    print("Inserting values into the heap:")
    for value in test_values:
        heappush(heap, value)
        print(f"Heap after inserting {value}: {heap[1:]}")

    # 값 삭제 테스트 (heappop)
    print("\nRemoving values from the heap:")
    while len(heap) > 1:
        popped_value = heappop(heap)
        print(f"Removed value: {popped_value}, Current heap: {heap[1:]}")
