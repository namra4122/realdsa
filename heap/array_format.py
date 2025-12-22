# Note: THIS IS MAX-HEAP IF WANT MIN-HEAP CHANGE THE COMPARISION SIGN
class Heap:
    def __init__(self):
        self.data = []

    def heapify_nlongn(self, data: list[int]):
        for i in data:
            self.insert(i)

    def heapify(self, data: list[int]):
        self.data = data
        size = len(self.data)
        for i in range(size // 2 - 1, -1, -1):
            self.bubbleDown(i, size)

    def bubbleUp(self, idx: int):
        if idx == 0:
            return idx

        parent_idx = (idx - 1) // 2

        if self.data[parent_idx] >= self.data[idx]:
            return idx

        self.data[parent_idx], self.data[idx] = self.data[idx], self.data[parent_idx]
        return parent_idx

    def insert(self, value: int):
        self.data.append(value)
        idx = len(self.data) - 1

        while idx > 0:
            new_idx = self.bubbleUp(idx)
            if new_idx == idx:
                break
            idx = new_idx

    def bubbleDown(self, idx: int, size: int):
        while True:
            l = 2 * idx + 1
            r = 2 * idx + 2
            lg = idx

            if l < size and self.data[l] > self.data[lg]:
                lg = l

            if r < size and self.data[r] > self.data[lg]:
                lg = r

            if lg == idx:
                break

            self.data[idx], self.data[lg] = self.data[lg], self.data[idx]
            idx = lg

    def delete(self):
        if len(self.data) == 0:
            return None

        root = self.data[0]
        size = len(self.data)
        self.data[0] = self.data[size - 1]
        self.data = self.data[: size - 1]

        idx = 0
        self.bubbleDown(idx, len(self.data))
        return root

    def __str__(self):
        return ", ".join(map(str, self.data))


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
print(f"[{h}]")
del_el = h.delete()
print(f"Deleted item: {del_el}")
del_el = h.delete()
print(f"Deleted item: {del_el}")
del_el = h.delete()
print(f"Deleted item: {del_el}")
print(f"[{h}]")

h1 = Heap()
d = [10, 6, 5, 15, 7, 4, 10, 1, 0]
h1.heapify(d)
print(f"[{h1}]")
