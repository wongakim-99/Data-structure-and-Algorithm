class Node: # 노드 생성 
    def __init__(self, item):
        self.item = item 
        self.left = None   # Node는 자기 자신의 값인 item과 자식의 위치인 left와 right를 가진다.
        self.right = None

# 각 노드를 엮어주기 위해서 BinaryTree생성
class BinaryTree(): 
    def __init__(self):
        self.root = None
    
    def self_root(self, node):
        self.root = node

    # 전위 순회
    def pre_order(self, node):
        if node:
            print(node.item)
            self.pre_order(node.left)
            self.pre_order(node.right)
        
    # 중위 순회
    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.item)
            self.in_order(node.right)
    
    # 후위 순회
    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.item)

if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print("Pre-order traversal: \n", end='')
    tree.pre_order(tree.root)
    print()

    
    print("In-order traversal: \n", end='')
    tree.in_order(tree.root)
    print()

    print("Post-order traversal: \n", end='')
    tree.post_order(tree.root)
    print()