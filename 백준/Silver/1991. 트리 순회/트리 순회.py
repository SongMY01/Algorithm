import sys
input = sys.stdin.readline

# 노드 저장 : { 'A': ['B', 'C'], ... }
tree = {}

N = int(input())
for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

# 전위순회 : Root → Left → Right
def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(tree[node][0])
    preorder(tree[node][1])

# 중위순회 : Left → Root → Right
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    print(node, end='')
    inorder(tree[node][1])

# 후위순회 : Left → Right → Root
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()