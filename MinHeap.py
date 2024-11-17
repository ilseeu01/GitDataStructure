def heappush(heap, n):
    heap.append(n)
    i = len(heap) - 1
    while i != 1:
        pi = i//2 # parent index
        if n >= heap[pi]:
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
        if i < size and heap[i] > heap[i+1]:
            i += 1
        if last <= heap[i]:
            break
        heap[pi] = heap[i]
        pi = i
        i *= 2

    heap[pi] = last
    heap.pop()
    return root

