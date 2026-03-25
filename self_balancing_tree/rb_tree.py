class Node:
    def __init__(self, data, black = True):
        self.data = data
        self.black = black
        self.left: Node|None = None
        self.right: Node|None = None
        self.parent: Node|None = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(data=None, black=True)
        self.root = self.NIL

    def _rotate_left(self, node):
        right_node = node.right
        node.right = right_node.left

        if right_node.left != self.NIL:
            right_node.left.parent = node

        right_node.parent = node.parent

        if node.parent is None:
            self.root = right_node
        elif node == node.parent.left:
            node.parent.left = right_node
        else:
            node.parent.right = right_node

        right_node.left = node
        node.parent = right_node  

    def _rotate_right(self, node):
        left_node = node.left
        node.left = left_node.right

        if left_node.right != self.NIL:
            left_node.right.parent = node

        left_node.parent = node.parent

        if node.parent is None:
            self.root = left_node
        elif node == node.parent.left:
            node.parent.left = left_node
        else:
            node.parent.right = left_node

        left_node.right = node
        node.parent = left_node

    def _fix_insert(self, node):
        while node.parent and not node.parent.black:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if not uncle.black:
                    node.parent.black = True
                    uncle.black = True
                    node.parent.parent.black = False
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    node.parent.black = True
                    node.parent.parent.black = False
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.black:
                    node.parent.black = True
                    uncle.black = True
                    node.parent.parent.black = False
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.black = True
                    node.parent.parent.black = False
                    self._rotate_left(node.parent.parent)

        self.root.black = True

    def insert(self, data: int):
        new_node = Node(data, False)
        new_node.left = new_node.right = self.NIL

        parent = None
        curr = self.root

        while curr != self.NIL:
            parent = curr

            if new_node.data < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.data <= parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        self._fix_insert(new_node)

    def search(self, value, node = None):
        if node is None:
            node = self.root

        if node == self.NIL or value == node.data:
            return node

        if value < node.data:
            return self.search(value, node.left)
        
        return self.search(value, node.right)

    def minimum(self, node = None):
        if node == None:
            node = self.root

        while node.left != self.NIL:
            node = node.left

        return node
    
    def _transplant(self, u,v):
        if u.parent == None:
            self.root = v
        elif u.parent.right == u:
            u.parent.left = v
        else:
            u.parent.right = v

        v.parent = u.parent

    def _fix_delete(self, node):
        while node != self.root and node.black:
            if node == node.parent.left:
                temp_node = node.parent.right

                if not temp_node.black:
                    temp_node.black = True
                    node.parent.black= False
                    self._rotate_left(node.parent)
                    temp_node = node.parent.right

                if temp_node.left.black and temp_node.right.black:
                    temp_node.black = False
                    node = node.parent
                else:
                    if temp_node.right.black:
                        temp_node.left.black = True
                        temp_node.black = False
                        self._rotate_right(temp_node)
                        temp_node = node.parent.right

                    temp_node.black = node.parent.black
                    node.parent.black = True
                    temp_node.right.black = True
                    self._rotate_left(node.parent)
                    node = self.root
            else:
                temp_node = ndoe.parent.left
                if not temp_node.black:
                    temp_node.black
                    node.parent.black = False
                    self._rotate_right(node.parent)
                    temp_node = node.parent.left
                if temp_node.right.black and temp_node.left.black:
                    temp_node.black = False
                    node = node.parent
                else:
                    if temp_node.left.black:
                        temp_node.right.black = True
                        temp_node.black = False
                        self._rotate_left(temp_node)
                        temp_node = node.parent.left

                    temp_node.black = node.parent.black
                    node.parent.black = True
                    temp_node.left.black = True
                    self._rotate_right(node.parent)
                    node = self.root

        node.black = True

    def delete(self, value):
        node = self.search(value)
        if node == self.NIL:
            print(f"Ohh paji ee value {value} toh sada tree vich hai hi nahi")
            return
        
        temp_node = node
        temp_node_black = temp_node.black

        if node.left == self.NIL:
           x = node.right
           self._transplant(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            self._transplant(node, node.left)
        else:
            temp_node = self.minimum(node.right)
            temp_node_black = temp_node.black
            x = temp_node.right
            if temp_node.parent == node:
                x.parent = temp_node
            else:
                self._transplant(temp_node, temp_node.right)
                temp_node.right = node.right
                temp_node.parent.right = temp_node
            
            self._transplant(node, temp_node)
            temp_node.left = node.left
            temp_node.left.parent = temp_node
            temp_node.black = node.black

        if temp_node_black:
            self._fix_delete(x)

    def inorder(self,res, node):
        if node == self.NIL:
            return
        
        self.inorder(res, node.left)
        res.append(node.data)
        self.inorder(res, node.right)

    def __str__(self):
        res = []
        self.inorder(res, self.root)
        return ", ".join(map(str, res))


rbtree = RedBlackTree()
rbtree.insert(10)
rbtree.insert(3)
rbtree.insert(4)
rbtree.insert(15)
rbtree.insert(14)
rbtree.insert(16)
rbtree.insert(2)
print(rbtree)
