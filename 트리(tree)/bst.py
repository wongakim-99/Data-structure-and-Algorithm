import sys

class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def set_root(self, node):
        self.root = node



#########################################################################
######################################################################    
    # 삽입함수 -> 재귀버젼
    def insertRecursive(self, current, data):
        if data < current.item:
            if current.left is None:
                current.left = Node(data)
            else:
                self.insertRecursive(current.left, data)
        else:
            if current.right is None:
                current.right = Node(data)
            else:
                self.insertRecursive(current.right, data)
    
    # 삽입함수 -> 반복문 버젼
    def insertIterative(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        
        current = self.root
        parent = None

        while current:
            parent = current
            if data < current.item:
                current = current.left
            else:
                current = current.right
        
        if data < parent.item:
            parent.left = node
        else:
            parent.right = node

##############################삽입함수 통제##############################
    def insert(self, data, use_recursive = True):
        if use_recursive:
            if self.root is None:
                self.root = Node(data)
            else:
                self.insertRecursive(self.root, data)
        else:
            self.insertIterative(data)
#########################################################################
#########################################################################



###############################탐색할 키 값###############################
    def searchIterative(self, data):
        node = self.root
        while node:
            if node.item == data:
                return node # 노드를 반환
            elif data < node.item:
                node = node.left
            else:
                node = node.right
        return None  # 노드를 찾지 못한 경우 - None을 반환
    
    def searchRecursive(self, node, data):
        if node is None or node.item == data:
            return node
        elif data < node.item:
            return self.searchRecursive(node.left, data)
        else:
            return self.searchRecursive(node.right, data)

    def search(self, data, use_recursive = True):
        if use_recursive:
            self.searchRecursive(self.root, data)
        else:
            self.searchIterative(data)
#########################################################################
#########################################################################



    # 전위 순회
    def pre_order(self, node):
        if node:
            print(node.item, end=' ')
            self.pre_order(node.left)
            self.pre_order(node.right)
        
    # 중위 순회
    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.item, end=' ')
            self.in_order(node.right)
    
    # 후위 순회
    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.item, end=' ')

if __name__ == "__main__":
    tree = BinaryTree()
    # 노드 삽입 (재귀 버전 사용)
    tree.insert(1, use_recursive=True)
    tree.insert(2, use_recursive=True)
    tree.insert(3, use_recursive=True)
    tree.insert(4, use_recursive=True)
    tree.insert(5, use_recursive=True)
    tree.insert(6, use_recursive=True)
    tree.insert(7, use_recursive=True)

    print("Pre-order traversal (recursive inserts): ", end='')
    tree.pre_order(tree.root)
    print()

    # 새로운 트리 생성
    tree2 = BinaryTree()
    # 노드 삽입 (반복문 버전 사용)
    tree2.insert(1, use_recursive=False)
    tree2.insert(2, use_recursive=False)
    tree2.insert(3, use_recursive=False)
    tree2.insert(4, use_recursive=False)
    tree2.insert(5, use_recursive=False)
    tree2.insert(6, use_recursive=False)
    tree2.insert(7, use_recursive=False)

    print("Pre-order traversal (iterative inserts): ", end='')
    tree2.pre_order(tree2.root)
    print()

    key = int(sys.stdin.readline())
    result = tree.search(key)

    if result:
        print(f"key {key} found is the tree")
    else:
        print(f"key {key} not found in the tree")
