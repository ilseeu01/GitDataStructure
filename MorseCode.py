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
    