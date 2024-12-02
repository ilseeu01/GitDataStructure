from BinSrchTree import *

class BinSet:
    def __init__(self, name):
        self.root = None
        self.name = name

    def add(self):
        print(f"{self.name} 집합의 원소를 입력 (종료하려면 음수 입력): ")
        while True:
            user_input = input()
            num = 0
            sign = 1
            is_number = False
            keys = []

            for char in user_input + ' ':
                if char == ' ':
                    if is_number:
                        keys.append(sign * num)
                        num = 0
                        sign = 1
                        is_number = False
                elif char == '-':
                    sign = -1
                elif '0' <= char <= '9':
                    num = num * 10 + int(char)
                    is_number = True

            for key in keys:
                if key < 0:
                    return
                new_node = BSTNode(key, None)
                self.root = insert_bst(self.root, new_node)

    def add_key(self, key):
        """차집합 등을 위해 키를 직접 추가합니다."""
        new_node = BSTNode(key, None)
        self.root = insert_bst(self.root, new_node)

    def search(self, key):
        return search_bst(self.root, key) is not None

    def is_empty(self):
        return self.root is None

    def union(self, rhs):
        self._traverse_and_add(rhs.root)

    def _traverse_and_add(self, node):
        if node is not None:
            self.add_key(node.key)
            self._traverse_and_add(node.left)
            self._traverse_and_add(node.right)

    def difference(self, rhs):
        """자기 집합에서 rhs 집합의 원소를 제거하여 차집합을 구성"""
        def traverse_and_remove(node):
            """rhs 집합에 있는 원소를 현재 집합에서 삭제"""
            if node is not None:
                if rhs.search(node.key):  # rhs 집합에 현재 원소가 있으면 삭제
                    self.root = delete_bst(self.root, node.key)
                traverse_and_remove(node.left)
                traverse_and_remove(node.right)

        traverse_and_remove(rhs.root)


    def inorder_traverse(self):
        print_inorder(self.root)
        print()


if __name__ == "__main__":
    # 집합 A와 B 생성
    A = BinSet("A") #클래스의 name 속성
    B = BinSet("B")

    A.add()
    B.add()

    # 중위 순회로 출력
    print("A 집합:")
    A.inorder_traverse()

    print("B 집합:")
    B.inorder_traverse()

    # 원소 검색
    print("A 집합에 9가 있는가?", A.search(9))  # True
    print("B 집합에 14가 있는가?", B.search(14))  # False

    # 합집합
    A.union(B)
    print("A ∪ B:")
    A.inorder_traverse()

    # 차집합
    A.difference(B)
    print("A - B:")
    A.inorder_traverse()

    # 공집합 확인
    C = BinSet("C")
    print("C는 공집합인가?", C.is_empty())  # True


    

