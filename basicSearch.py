def binary_search(A, key, low, high):
    if (low > high):
        return -1
    
    middle = (low + high) // 2
    if (A[key] < middle):
        binary_search(A, key, low, middle-1)
    elif (A[key] > middle):
        binary_search(A, key, middle+1, high)
    else:
        print("list[key] : ", middle)
        return middle
    

if __name__ == "__main__":
    listA = [1,2,3,4,5,6,7,8,9]
    binary_search(listA, 3, 0, 10)