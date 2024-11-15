from BinaryTree import TNode

table = [
    ('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'),
    ('E', '.'), ('F', '..-.'), ('G', '--.'), ('H', '....'),
    ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
    ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'),
    ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'),
    ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
    ('Y', '-.--'), ('Z', '--..')
]

def encode(ch):
    idx = ord(ch) - ord('A')
    return table[idx][1]

def decode_slow(code):
    for e in table:
        if code == e[1]:  # e[1]은 모스 부호
            return e[0]   # e[0]은 알파벳
    return None

def make_morse_tree():
    root = TNode(None, None, None)
    for tp in table:
        code = tp[1]
        node = root
        for c in code:
            if c == '.':
                if node.left == None:
                    node.left = TNode(None, None, None)
                node = node.left
            elif c == '-':
                if node.right == None:
                    node.right = TNode(None, None, None)
                node = node.right
        node.data = tp[0]
    return root

def decode(root, code):
    node = root
    for c in code:
        if c == '.':
            node = node.left
        elif c == '-':
            node = node.right
    return node.data

if __name__ == "__main__":
    # 모스 부호 트리 생성
    root = make_morse_tree()

    # 테스트할 문자열
    test_str = "SOS"
    print(f"Input String: {test_str}")

    # 문자열을 모스 부호로 인코딩
    encoded_list = [encode(ch) for ch in test_str]
    encoded_str = ' '.join(encoded_list)
    print(f"Encoded Morse Code: {encoded_str}")

    # 모스 부호를 다시 문자열로 디코딩
    decoded_list = [decode(root, code) for code in encoded_str.split()]
    decoded_str = ''.join(decoded_list)
    print(f"Decoded String: {decoded_str}")

