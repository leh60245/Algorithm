import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

n = int(input())
graph = dict()
for _ in range(n):
    p, a, b = map(str, input().split())
    graph[p] = [a, b]


def preorder(node):
    if node == ".":
        return
    print(node, end="")
    preorder(graph[node][0])
    preorder(graph[node][1])

def inorder(node):
    if node == ".":
        return
    inorder(graph[node][0])
    print(node, end="")
    inorder(graph[node][1])

def postorder(node):
    if node == ".":
        return
    postorder(graph[node][0])
    postorder(graph[node][1])
    print(node, end="")

preorder("A")
print()
inorder("A")
print()
postorder("A")