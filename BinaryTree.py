from Queue import CircularQueue 

class TNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def preorder(n):
    if n is not None:
        print(n.data, end = ' ')
        preorder(n.left)
        preorder(n.right)

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end = ' ')
        inorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end = ' ')

def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end = ' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)
# 재귀 함수를 사용하는 것이 전역변수 count를 사용해서 1씩 증가시키는 것보다 효율적이다 
# 부수효과가 존재하기 때문이다

def count_leaf(n):
    if n is None:
        return 0
    elif n.left == None and n.right == None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)

def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if hLeft > hRight:
        return hLeft + 1
    else:
        return hRight + 1

if __name__ == "__main__":
    # 이진 트리 생성
    #       A
    #      / \
    #     B   C
    #    / \   \
    #   D   E   F

    n1 = TNode('D')
    n2 = TNode('E')
    n3 = TNode('F')
    n4 = TNode('B', n1, n2)
    n5 = TNode('C', None, n3)
    root = TNode('A', n4, n5)

    # 전위 순회 출력
    print("Preorder Traversal:")
    preorder(root)
    print()

    # 중위 순회 출력
    print("Inorder Traversal:")
    inorder(root)
    print()

    # 후위 순회 출력
    print("Postorder Traversal:")
    postorder(root)
    print()

    print("Level-order Traversal:")
    levelorder(root)
    print()

    print("Count node:")
    print(count_node(root))

    print("Count leaf:")
    print(count_leaf(root))

    print("Calculate height:")
    print(calc_height(root))
