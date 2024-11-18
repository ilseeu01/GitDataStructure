from BinSrchTree import search_bst, search_max_bst, search_min_bst, search_value_bst, insert_bst, delete_bst, BSTNode


class BSTMap():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def fineMax(self):
        return search_max_bst(self.root)
    
    def fineMin(self):
        return search_min_bst(self.root)
    
    def search(self, key):
        return search_bst(self.root, key)
    
    def searchValue(self, value):
        return search_value_bst(self.root, value)
    
    def insert(self, key, value=None):
        n = BSTNode(key, value)
        self.root = insert_bst(self.root, n)

    def delete(self, key):
        self.root = delete_bst(self.root, key)

    def display(self, msg=' BTSMap: '):
        print(msg, end='')
        inorder(self.root)
        print()

if __name__ == '__main__':
    data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
    value = ['삼오', '일팔', '영칠', '이육', '일이', '영삼', '육팔', '이이', '삼영', '구구']

    map = BSTMap()
    map.display('삽입 전 : ')
    for i in range(len(data)):
        map.insert(data[i], value[i])
        map.display(f'{data[i]} 삽입 : ')

    print('최대 키 : ', map.findMax().key)
    print('최소 키 : ', map.findMin().key)
    print('26 탐색 : ', '성공' if map.search(26) != None else '실패')
    print('25 탐색 : ', '성공' if map.search(25) != None else '실패')
    print('일팔 탐색 : ', '성공' if map.searchValue('일팔') != None else '실패')
    print('일칠 탐색 : ', '성공' if map.searchValue('일칠') != None else '실패')

    map.delete(3)
    map.display('delete 3 : ')
    map.delete(68)
    map.display('delete 68 : ')
    map.delete(18)
    map.display('delete 18 : ')    
    map.delete(35)
    map.display('delete 35 : ')

