# Note: THIS IS MAX-HEAP IF WANT MIN-HEAP CHANGE THE COMPARISION SIGN
from collections import deque

class TreeNode:
    def __init__(self, data: int):
        self.data = data
        self.right = None
        self.left = None
        self.parent = None


class Heap:
    def __init__(self):
        self.root = None
        self.size = 0

    def bubbleUp(self, node: TreeNode | None):
        while node.parent and node.data > node.parent.data:
            node.data, node.parent.data = node.parent.data, node.data
            node = node.parent

    def insert(self, data: int):
        newNode = TreeNode(data)
        if self.root is None:
            self.root = newNode
            self.size = 1
            return

        path = format(self.size + 1, "b")[1:]
        curr = self.root

        for bit in path[:-1]:
            if bit == "0":
                curr = curr.left
            else:
                curr = curr.right

        if path[-1] == "0":
            curr.left = newNode
        else:
            curr.right = newNode

        newNode.parent = curr
        self.size += 1

        self.bubbleUp(newNode)
        return

    def getLastNode(self):
        path = format(self.size, "b")[1:]
        curr = self.root
        for bit in path:
            if bit == "0":
                curr = curr.left
            else:
                curr = curr.right

        return curr

    def detachNode(self, node: TreeNode | None):
        parent = node.parent

        if parent.left == node:
            parent.left = None
        elif parent.right == node:
            parent.right = None

        node.parent = None

    def bubbleDown(self, node: TreeNode | None):
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

    def delete(self):
        if self.size == 0:
            return "Heap Empty"

        removedNode = self.root.data

        if self.size == 1:
            self.root = None
            self.size = 0
            return removedNode

        lastNode = self.getLastNode()
        self.root.data = lastNode.data

        self.detachNode(lastNode)
        self.size -= 1

        self.bubbleDown(self.root)
        return removedNode

    def __str__(self):
        if not self.root:
            return "Empty Heap"

        q = deque([self.root])
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


h = Heap()
h.insert(10)
h.insert(6)
h.insert(5)
h.insert(15)
h.insert(7)
h.insert(4)
h.insert(10)
h.insert(1)
h.insert(0)
print(h)
del_el = h.delete()
print(f"Deleted item: {del_el}")
del_el = h.delete()
print(f"Deleted item: {del_el}")
del_el = h.delete()
print(f"Deleted item: {del_el}")
print(h)
