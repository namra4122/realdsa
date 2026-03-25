from typing import List


class QuickSort:
    def __init__(self, data: List) -> None:
        self.data = data

    def _partition(self, l: int, h: int) -> int:
        # pivot = self.data[l]
        # b = l

        # for i in range(l + 1, h + 1):
        #     if self.data[i] < pivot:
        #         b += 1
        #         self.data[i], self.data[b] = self.data[b], self.data[i]

        # self.data[l], self.data[b] = self.data[b], self.data[l]
        # return b
        pivot = self.data[l]
        i=l+1
        j=h
        
        while (True):
            while( self.data[i] < pivot and i<=h):
                i+=1
            while(self.data[j] >= pivot and j>=l):
                j-=1
            
            if i<=j:
                break

            self.data[i], self.data[j]=self.data[j], self.data[i]
        return i

    def _recur_sort(self, l: int, h: int):
        if l < h:
            pivot_iloc = self._partition(l, h)
            self._recur_sort(l, pivot_iloc - 1)
            self._recur_sort(pivot_iloc + 1, h)

    def sort(self) -> List[int]:
        self._recur_sort(0, len(self.data) - 1)
        return self.data

    def __str__(self) -> str:
        return ",".join(map(str, self.data))


data = QuickSort([22, 3, 4, 5, 1, 2, 388, 6, 9, 8, 23])
data.sort()
print(data)
