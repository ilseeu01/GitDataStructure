# BST : Binary Search Tree
class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

def search_bst(n, key):
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)

def search_bst_iter(n, key):
    while n != None:
        if key == n.key:
            return n
        elif key < n.key:
            n = n.left
        else:
            n = n.right
    return None

def search_value_bst(n, value):
    if n == None:
        return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value)
    if res is not None:
        return res
    else:
        return search_value_bst(n.right, value)
    
def search_max_bst(n):
    while n != None and n.right != None:
        n = n.right
    return n

def search_min_bst(n):
    while n != None and n.left != None:
        n = n.left
    return n

def insert_bst(root, node):
    if root == None:
        return node
    if node.key == root.key:
        return root
    if node.key < root.key:
        root.left = insert_bst(root.left, node)
    else:
        root.right = insert_bst(root.right, node)
    return root

def delete_bst(root, key):
    if root == None:
        return root
    
    if key < root.key:
        root.left = delete_bst(root.left, key)
    elif key > root.key:
        root.right = delete_bst(root.right, key)
    else:
        if root.left == None:
            return root.right
        if root.right == None:
            return root.left
        
        succ = search_min_bst(root.right)
        root.key = succ.key
        root.value = succ.value
        root.right = delete_bst(root.right, succ.key)

    return root

def print_inorder(n):
    """중위 순회로 트리 출력 (key, value) 형태로 출력"""
    if n is not None:
        print_inorder(n.left)
        print(f"({n.key}, {n.value})", end=" ")
        print_inorder(n.right)

if __name__ == "__main__":
    # 새로운 이진 탐색 트리 생성
    root = None

    # 테스트할 노드 데이터 (key, value) 형태
    nodes = [(50, 'A'), (30, 'B'), (70, 'C'), (20, 'D'), (40, 'E'), (60, 'F'), (80, 'G')]

    # 노드 삽입 테스트
    print("Inserting nodes:")
    for key, value in nodes:
        root = insert_bst(root, BSTNode(key, value))
        print_inorder(root)
        print()

    # 노드 검색 테스트
    print("\nSearching for key 40:")
    result = search_bst(root, 40)
    if result:
        print(f"Found node: ({result.key}, {result.value})")
    else:
        print("Node not found.")

    # 값 검색 테스트
    print("\nSearching for value 'C':")
    result = search_value_bst(root, 'C')
    if result:
        print(f"Found node: ({result.key}, {result.value})")
    else:
        print("Node not found.")

    # 최대값, 최소값 검색 테스트
    max_node = search_max_bst(root)
    min_node = search_min_bst(root)
    if max_node:
        print(f"\nMax node: ({max_node.key}, {max_node.value})")
    if min_node:
        print(f"Min node: ({min_node.key}, {min_node.value})")

    # 노드 삭제 테스트
    print("\nDeleting key 30:")
    root = delete_bst(root, 30)
    print_inorder(root)
    print()

    print("Deleting key 70:")
    root = delete_bst(root, 70)
    print_inorder(root)
    print()

    print("Deleting key 50:")
    root = delete_bst(root, 50)
    print_inorder(root)
    print()      