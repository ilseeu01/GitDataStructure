from HashLinearProb import hashFn
from LinkedStack import Node, LinkedStack

M = 13
table = [None] * M

def insert(key):
    k = hashFn(key)
    n = Node(key)
    n.link = table[k]
    table[k] = n

def search(key):
    k = hashFn(key)
    n = table[k]
    while n is not None:
        if n.data == key:
            return n.data