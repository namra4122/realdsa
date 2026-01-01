from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data: int = data
        self.parent: TreeNode | None = None
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def printTree(root):
    if not root:
        return "Empty Heap"

    q = deque([root])
    result = []

    while q:
        level_size = len(q)
        level = []

        for _ in range(level_size):
            node = q.popleft()
            level.append(str(node.data))

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(" ".join(level))

    return "\n".join(result)


def bubbleDown(node: TreeNode | None):
    print("============bubbleDown: ", node.data)
    while node.left is not None or node.right is not None:
        temp = node

        if node.left and node.left.data > temp.data:
            temp = node.left
        if node.right and node.right.data > temp.data:
            temp = node.right

        if temp == node:
            break

        node.data, temp.data = temp.data, node.data
        node = temp


def heapify(node: TreeNode | None):
    if node is None:
        return
    print("============heapify: ", node.data)

    heapify(node.left)
    heapify(node.right)

    bubbleDown(node)


def mergeTree(t1: TreeNode, t2: TreeNode):
    curr: TreeNode = t1
    while curr and curr.right:
        curr = curr.right

    curr.right = t2

    heapify(t1)


tree_1 = TreeNode(10)
tree_1_1 = TreeNode(6)
tree_1_0 = TreeNode(5)
tree_1_00 = TreeNode(2)

tree_1.left = tree_1_0
tree_1.right = tree_1_1
tree_1_0.parent = tree_1
tree_1_1.parent = tree_1
tree_1_0.left = tree_1_00
tree_1_00.parent = tree_1_0


tree_2 = TreeNode(12)
tree_2_0 = TreeNode(7)
tree_2_1 = TreeNode(9)
tree_2.left = tree_2_0
tree_2.right = tree_2_1
tree_2_0.parent = tree_2
tree_2_1.parent = tree_2

mergeTree(tree_1, tree_2)
a = printTree(tree_1)
print(a)
