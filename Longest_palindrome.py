def is_palindrome(subsequence):
    """부분 문자열이 회문인지 검사"""
    return subsequence == subsequence[::-1] #O(n) 부분문자열의 길이가 n이면 n의 시간복잡도를 가짐

def longest_palindrome(sequence):
    n = len(sequence)
    max_length = 1
    start_index = 0

    # 모든 부분 문자열에 대해 회문 검사
    for i in range(n): #O(n) i가 n번 반복함
        for j in range(i + 1, n + 1): #O(n) #평균적으로 n회 반복함
            subsequence = sequence[i:j]  # 부분 문자열 생성

            if is_palindrome(subsequence):
                length = j - i
                if length > max_length:
                    max_length = length
                    start_index = i

    print(f"Answer is from {start_index} with length {max_length}.")


def stringAlignment(text):
    sequence = ''
    for c in text:
        if not c in " ,'": # 문자열의 길이만큼 반복하므로, O(n)을 가짐
            sequence += c
    return sequence

# 총 bigO(n^3)을 갖는다고 볼 수 있다.

if __name__ == "__main__":
    
    text = '1  6  3  1  2  2  1  3  1  2  1  3  6  1'
    sequence = stringAlignment(text)
    longest_palindrome(sequence)
    
    text2 = 'eye'
    sequence2 = stringAlignment(text2)
    longest_palindrome(sequence2)

    text3 = 'madam, I\'m adam'
    sequence3 = stringAlignment(text3)
    longest_palindrome(sequence3)

    text4 = 'race car'    
    sequence4 = stringAlignment(text4)
    longest_palindrome(sequence4)

