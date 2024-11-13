# Hash : 해시테이블을 사용한 구조
# LinearProbing : 충돌이 발생한 위치에서 다음 빈 공간을 순차적으로 찾음  

M = 13
table = [None] * M

def hashFn(key):
    return key % M

def insert(key):
    i = hashFn(key)
    count = M
    while count > 0:
        if table[i] == None or table[i] == -1:
            break
        i = (i+1) % M
        count -= 1

    if count > 0:
        table[i] = key

def search(key):
    i = hashFn(key)
    count = M
    while count > 0:
        if table[i] == None:
            return None
        elif table[i] == key:
            return table[i]
        i = (i+1) % M
        count -= 1

    return None

def delete(key):
    i = hashFn(key)
    count = M
    while count > 0:
        if table[i] == None:
            return
        elif table[i] == key:
            table[i] = -1
        i = (i+1) % M
        count -= 1
    return


    
if __name__ == "__main__":
    # 예제 데이터 삽입
    keys_to_insert = [10, 22, 31, 4, 15, 28, 17, 88, 59]
    print("Inserting keys:", keys_to_insert)
    for key in keys_to_insert:
        insert(key)
    print("Hash Table after insertion:", table)

    # 검색 테스트
    keys_to_search = [10, 88, 4, 100]  # 마지막 100은 존재하지 않는 키
    for key in keys_to_search:
        result = search(key)
        if result is not None:
            print(f"Key {key} found in hash table.")
        else:
            print(f"Key {key} not found in hash table.")

    # 삭제 테스트
    keys_to_delete = [10, 4]
    print("Deleting keys:", keys_to_delete)
    for key in keys_to_delete:
        delete(key)
    print("Hash Table after deletion:", table)

    # 삭제 후 검색 테스트
    for key in keys_to_delete:
        result = search(key)
        if result is not None:
            print(f"Key {key} found in hash table after deletion (error).")
        else:
            print(f"Key {key} not found in hash table after deletion (expected).")