class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self):
        self.head = None

    def add(self, data: int):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node
        new_node.prev = curr
        return

    def insert(self, index: int, data: int):
        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
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
        if curr.next:
            curr.next.prev = new_node
        new_node.prev = curr
        curr.next = new_node
        return

    def remove(self, index: int) -> None:
        if self.head is None:
            print("List empty hai")
            return

        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        curr_idx = 0
        curr = self.head
        while curr_idx != index - 1:
            if curr.next:
                curr = curr.next
                curr_idx += 1
            else:
                print(
                    f"LinkedList has size of {curr_idx + 1} can't remove at {
                        index
                    } index"
                )
                return

        curr.next = curr.next.next
        if curr.next:
            curr.next.prev = curr
        return

    def pop(self) -> int | None:
        if self.head is None:
            print("lisy empty hai")
            return None

        if self.head.next is None:
            data = self.head.data
            self.head = None
            return data

        curr = self.head
        while curr.next.next:
            curr = curr.next

        data = curr.next.data
        curr.next = None
        return data

    def get(self, index: int) -> int | str:
        if self.head is None:
            return "list empty hai"
        curr_idx = 0
        curr = self.head
        while curr and curr_idx < index:
            curr = curr.next
            curr_idx += 1

        if curr is None:
            return f"{index}th exist nahi karti"

        return curr.data

    def search(self, value: int) -> str:
        curr_idx = 0
        curr = self.head
        while curr is not None and curr.data != value:
            curr_idx += 1
            curr = curr.next

        if curr is None:
            return f"koi node nahi hai with value: {value}"

        return f"yeh lo index: {curr_idx} aur uski value:{curr.data}"

    def __str__(self):
        values = []
        curr = self.head
        while curr:
            values.append(str(curr.data))
            curr = curr.next

        return " <-> ".join(values) + " <-> end"


dll = DoublyLL()
dll.add(5)
dll.add(5)
dll.add(3)
dll.add(1)
dll.add(2)
dll.add(3)
dll.add(1)
dll.add(2)
dll.insert(index=1, data=4)
dll.remove(1)
dll.pop()
a = dll.get(0)
print(a)
b = dll.search(6)
print(b)
print(dll)
