from BinaryTree import calc_height, count_node, count_leaf, levelorder
from Queue import CircularQueue 

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def calc_height_diff(n):
    if n == None:
        return 0
    return calc_height(n.left) - calc_height(n.right)

def rotateLL(A):
    B = A.left
    A.left = B.right
    B.right = A
    return B

def rotateRR(A):
    B = A.right
    A.right = B.left
    B.left = A
    return B

def rotateRL(A):
    B = A.right
    A.right = rotateLL(B)
    return rotateRR(A)

def rotateLR(A):
    B = A.left
    A.left = rotateRR(A)
    return rotateLL(B)

def insert_avl(root, node):
    if root == None:
        return node
    if node.key == root.key:
        return root
    if node.key < root.key:
        root.left = insert_avl(root.left, node)
    elif node.key > root.key:
        root.right = insert_avl(root.right, node)
    
    bf = calc_height_diff(root)

    if bf > 1:
        if node.key < root.left.key: #새로운 node.key가 root.left인지 확인
            return rotateLL(root)
        else:
            return rotateLR(root)
    elif bf < -1:
        if node.key > root.right.key: #새로 삽입된 node.key가 root.right에 삽입된건지 확인, 그 경우 bf가 2 이상이기 때문에 회전 필요함.
            return rotateRR(root)
        else:
            return rotateRL(root)
    return root

# def levelorder(root):
#     if root is not None:
#         print(f'{root.key}', end = ' ')
#         levelorder(root.left)
#         levelorder(root.right)

def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.key, end = ' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

if __name__ == '__main__':
    node = [7,8,9,2,1,5,3,6,4]
    root = None
    for i in node:
        n = BSTNode(i)
        root = insert_avl(root, n)
        print(f'BST({i}) : ', end= '')
        levelorder(root)
        print()
    
    print(f'노드의 개수 : {count_node(root)}')
    print(f'단말의 개수 : {count_leaf(root)}')
    print(f'트리의 높이 : {calc_height(root)}')

    
