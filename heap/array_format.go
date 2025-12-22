// Note: THIS IS MAX-HEAP IF WANT MIN-HEAP CHANGE THE COMPARISION SIGN

package main

import "fmt"

type ArrayHeap struct {
	data []int
}

func NewArrayHeap() *ArrayHeap {
	return &ArrayHeap{}
}

func bubbleUp(idx int, h ArrayHeap) int {
	var parent_idx int = (idx - 1) / 2

	if h.data[parent_idx] > h.data[idx] {
		return idx
	}

	h.data[parent_idx], h.data[idx] = h.data[idx], h.data[parent_idx]
	return parent_idx
}

func (h *ArrayHeap) Insert(value int) {
	h.data = append(h.data, value)
	idx := len(h.data) - 1

	for idx > 0 {
		new_idx := bubbleUp(idx, *h)
		if new_idx == idx {
			break
		}
		idx = new_idx
	}
}

func bubbleDown(h ArrayHeap, idx int, size int) {
	for true {
		l := 2*idx + 1
		r := 2*idx + 2
		lg := idx

		if l < size && h.data[l] > h.data[lg] {
			lg = l
		}

		if r < size && h.data[r] > h.data[lg] {
			lg = r
		}

		if lg == idx {
			break
		}

		h.data[idx], h.data[lg] = h.data[lg], h.data[idx]
		idx = lg
	}
}

func (h *ArrayHeap) Delete() (int, error) {
	if len(h.data) == 0 {
		return 0, fmt.Errorf("Heap is empty")
	}

	root := h.data[0]
	size := len(h.data)
	h.data[0] = h.data[size-1]
	h.data = h.data[:size-1]

	idx := 0
	bubbleDown(*h, idx, len(h.data))
	return root, nil
}

func (h *ArrayHeap) Heapify(data []int) {
	h.data = data
	size := len(h.data)
	for i := int(size/2) - 1; i >= 0; i-- {
		bubbleDown(*h, i, size)
	}
}

func (h *ArrayHeap) Print() {
	fmt.Println(h.data)
}

func main() {
	h := NewArrayHeap()
	d := []int{1, 2, 3, 4, 5, 6, 7}
	h.Heapify(d)
	h.Print()
	h.Insert(15)
	h.Insert(7)
	h.Insert(4)
	h.Insert(10)
	h.Insert(1)
	h.Insert(0)
	h.Print()
	del_el, err := h.Delete()
	if err != nil {
		panic(err)
	}
	fmt.Printf("Deleted item: %d\n", del_el)
	del_el_2, err := h.Delete()
	if err != nil {
		panic(err)
	}
	fmt.Printf("Deleted item: %d\n", del_el_2)
	del_el_3, err := h.Delete()
	if err != nil {
		panic(err)
	}
	fmt.Printf("Deleted item: %d\n", del_el_3)
	h.Print()
}
