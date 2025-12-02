class Node:
    def __init__(self, value:int):
        self.value = value
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None

    def add(self, value: int):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node
        return

    def insert(self, index: int, value: int) -> None:
        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        curr_idx = 0
        curr = self.head
        while curr and curr_idx < index - 1:
            curr = curr.next
            curr_idx += 1

        if curr is None:
            print(f"{index}th exist nahi karti")

        new_node.next = curr.next
        curr.next = new_node
        return


    def remove(self, index: int) -> None:
        curr_idx = 0
        curr = self.head
        while curr_idx != (index-1):
            if curr.next:
                curr = curr.next
                curr_idx += 1
            else:
                print(f"LinkedList has size of {curr_idx+1} can't remove at {index} index")
                return

        curr.next = curr.next.next
        return

    def pop(self) -> int|None:
        if self.head is None:
            print("list empty hai")
            return None

        if self.head.next is None:
            value = self.head.value
            self.head = None
            return value

        curr = self.head
        while curr.next.next:
            curr = curr.next

        value = curr.next.value
        curr.next = None
        return value

    def get(self, index: int) -> int|str|None:
        if self.head is None:
            return "list empty hai"
        curr_idx = 0
        curr = self.head
        while curr and curr_idx < index:
            curr = curr.next
            curr_idx += 1

        if curr is None:
            return f"{index}th exist nahi karti"

        return curr.value 

    def search(self, value: int) -> str:
        curr_idx = 0
        curr = self.head
        while curr is not None and curr.value != value:
            curr_idx += 1
            curr = curr.next

        if curr is None:
            return f"koi node nahi hai with value: {value}"

        return f"yeh lo index: {curr_idx} aur uski value:{curr.value}"

    def __str__(self):
        values = []
        curr = self.head
        while curr:
            values.append(str(curr.value))
            curr = curr.next
        return "->".join(values) + "->end"

sll = SinglyLL()
sll.add(5)
sll.add(5)
sll.add(3)
sll.add(1)
sll.add(2)
sll.add(3)
sll.add(1)
sll.add(2)
sll.insert(index=1, value=4)
sll.remove(1)
sll.pop()
a = sll.get(0)
print(a)
b = sll.search(3)
print(b)
print(sll)
