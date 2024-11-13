def hashFn(key, M):
    sum = 0
    for c in key:
        sum = sum + ord(c)
    return sum % M

if __name__ == "__main__":
    key = "hello"  # 예제 키
    M = 10         # 해시 테이블 크기
    hash_value = hashFn(key, M)
    print(f"The hash value for key '{key}' with table size {M} is: {hash_value}")
