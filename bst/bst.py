from collections import deque


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, num: int):
        newNode = Node(num)
        if self.root is None:
            self.root = newNode
            return

        curr = self.root

        while curr is not None:
            if curr.data > num and curr.left is not None:
                curr = curr.left
            elif curr.data < num and curr.right is not None:
                curr = curr.right
            else:
                break

        if curr.data >= num:
            curr.left = newNode
        else:
            curr.right = newNode

        return

    def preorder(self, res: list[int], node: Node | None):
        # Root -> Left -> Right
        if node is None:
            return

        res.append(node.data)

        self.preorder(res, node.left)
        self.preorder(res, node.right)

    def _preorder_itr(self):
        res = []
        stack = [self.root]

        while stack:
            node = stack.pop()
            res.append(node.data)

            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        print(res)

    def postorder(self, res: list[int], node: Node | None):
        # Left -> Right -> Root
        if node is None:
            return

        self.postorder(res, node.left)
        self.postorder(res, node.right)
        res.append(node.data)

    def _postorder_itr(self):
        res = []
        # Method - 1 using two stacks
        # stack_1 = [self.root]
        # stack_2 = []
        #
        # while stack_1:
        #     node = stack_1.pop()
        #     stack_2.append(node)
        #
        #     if node.left is not None:
        #         stack_1.append(node.left)
        #     if node.right is not None:
        #         stack_1.append(node.right)
        #
        # while stack_2:
        #     res.append(stack_2.pop().data)

        # Method - 2 using one stacks
        stack = []
        curr = self.root
        last = None

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                peek = stack[-1]
                if peek.right and last != peek.right:
                    curr = peek.right
                else:
                    res.append(peek.data)
                    last = stack.pop()

        print(res)

    def inorder(self, res: list[int], node: Node | None):
        # Left -> Root -> Right
        if node is None:
            return

        self.inorder(res, node.left)
        res.append(node.data)
        self.inorder(res, node.right)

    def _inorder_itr(self):
        res = []
        stack = []
        curr = self.root

        while curr is not None or len(stack) > 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.data)
            curr = curr.right

        print(res)

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

    def height(self):
        height = self._dfs_recur(self.root)
        bfs_height = self._bfs_recur(self.root)
        print(f"=========BFS:{bfs_height}")
        return height

    def _dfs_recur(self, node: Node):
        if not node:
            return -1  # this is if calculating nodes/level it will be 0

        left = self._dfs_recur(node.left)
        right = self._dfs_recur(node.right)

        return 1 + max(left, right)

    def _bfs_recur(self, node: Node | None):
        if not node:
            return -1  # this is if calculating nodes/level it will be 0

        level = -1  # this is if calculating nodes/level it will be 0

        q = deque([node])

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

            level += 1

        return level


bst = BST()
print("Press the num key to end to BST, and press `q` to end the script")

while True:
    ui = input("Button dbao: ")

    if ui == "q":
        break

    try:
        n = int(ui)
        bst.insert(n)
    except ValueError:
        print("BOLA THA BAS num key enter karo.. Yah toh PHIR `q` dbao")

res = []
bst.preorder(res, bst.root)
print(res)
print(bst.height())
