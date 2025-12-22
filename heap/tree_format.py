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
        if node is None:
            return

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
        if node.parent is None:
            return

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

    def _count_nodes(self, node: TreeNode):
        if node is None:
            return 0

        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def _heapify_recursive(self, node):
        if node is None:
            return

        self._heapify_recursive(node.left)
        self._heapify_recursive(node.right)

        self.bubbleDown(node)

    def heapify(self, node: TreeNode):
        self.root = node
        self.size = self._count_nodes(node)

        self._heapify_recursive(node)

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


# h = Heap()
# h.insert(10)
# h.insert(6)
# h.insert(5)
# h.insert(15)
# h.insert(7)
# h.insert(4)
# h.insert(10)
# h.insert(1)
# h.insert(0)
# print(h)
# del_el = h.delete()
# print(f"Deleted item: {del_el}")
# del_el = h.delete()
# print(f"Deleted item: {del_el}")
# del_el = h.delete()
# print(f"Deleted item: {del_el}")
# print(h)


# h1 = Heap()
# t = TreeNode(1)
# t1 = TreeNode(2)
# t2 = TreeNode(3)
# t3 = TreeNode(4)
# t4 = TreeNode(5)
# t5 = TreeNode(6)
# t6 = TreeNode(7)
#
# t.right = t1
# t.left = t2
# t1.parent = t
# t2.parent = t
#
# t1.right = t3
# t1.left = t4
# t3.parent = t1
# t4.parent = t1
#
# t2.right = t5
# t2.left = t6
# t5.parent = t2
# t6.parent = t2
#
# h1.heapify(t)
# h1.root = t
# print(h1)


h = Heap()
h.insert(1)
h.insert(2)
h.insert(3)
h.insert(4)
h.insert(5)
print(h)
print(f"Size: {h.size}")  # Should be 5
print(f"Deleted: {h.delete()}")  # Should be 5
print(f"Size: {h.size}")  # Should be 4
