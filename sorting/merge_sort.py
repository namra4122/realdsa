from typing import List


class MergeSort:
    def __init__(self, data: List) -> None:
        self.data = data

    def _merge(self,data, left_data, right_data) -> None:
        i=j=k=0

        while i<len(left_data) and j<len(right_data):
            if left_data[i]<right_data[j]:
                data[k] = left_data[i]
                i+=1
            else:
                data[k] = right_data[j]
                j+=1

            k+=1

        while i<len(left_data):
            data[k]=left_data[i]
            i+=1
            k+=1

        while j<len(right_data):
            data[k]=right_data[j]
            j+=1
            k+=1

    def _recur_sort(self, data: List[int]) -> List[int]:
        if len(data)>1:
            mid = len(data)//2
            left_data = data[:mid]
            right_data = data[mid:]

            self._recur_sort(left_data)
            self._recur_sort(right_data)

            self._merge(data, left_data, right_data)

        return data


    def sort(self) -> List[int]:
        self.data = self._recur_sort(self.data)
        return self.data

    def __str__(self) -> str:
        return ",".join(map(str, self.data))


data = MergeSort([22, 3, 4, 5, 1, 2, 388, 6, 9, 8, 0])
data.sort()
print(data)
