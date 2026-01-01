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

        if curr.data > num:
            curr.left = newNode
        else:
            curr.right = newNode

        return

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


bst = BST()
print("Press the num key to end to BST, and press `q` to end the script")

while True:
    ui = input("Button dbao: ")

    if ui == 'q':
        break
    
    try:
        n = int(ui)
        bst.insert(n)
    except ValueError:
        print("BOLA THA BAS num key enter karo.. Yah toh PHIR `q` dbao")

print(bst)
