// Note: THIS IS MAX-HEAP IF WANT MIN-HEAP CHANGE THE COMPARISION SIGN
package main

import (
	"fmt"
	"strings"
)

type TreeNode struct {
	data   int
	right  *TreeNode
	left   *TreeNode
	parent *TreeNode
}

type TreeHeap struct {
	root *TreeNode
	size int
}

func NewTreeHeap() *TreeHeap {
	return &TreeHeap{}
}

func (n *TreeNode) bubbleUp() {
	for n.parent != nil && n.data > n.parent.data {
		n.data, n.parent.data = n.parent.data, n.data
		n = n.parent
	}
}

func (h *TreeHeap) Insert(data int) {
	newNode := &TreeNode{data: data}

	if h.root == nil {
		h.root = newNode
		h.size = 1
		return
	}

	path := fmt.Sprintf("%b", h.size+1)[1:]
	curr := h.root

	for _, bit := range path[:len(path)-1] {
		if bit == '0' {
			curr = curr.left
		} else {
			curr = curr.right
		}
	}

	if path[len(path)-1] == '0' {
		curr.left = newNode
	} else {
		curr.right = newNode
	}

	newNode.parent = curr
	h.size += 1

	newNode.bubbleUp()
	return
}

func (h *TreeHeap) getLastNode() *TreeNode {
	path := fmt.Sprintf("%b", h.size)[1:]
	curr := h.root

	for _, bit := range path {
		if bit == '0' {
			curr = curr.left
		} else {
			curr = curr.right
		}
	}

	return curr
}

func detachNode(node *TreeNode) {
	parent := node.parent

	if parent.left == node {
		parent.left = nil
	} else if parent.right == node {
		parent.right = nil
	}

	node.parent = nil
}

func bubbleDown(node *TreeNode) {
	for node.left != nil || node.right != nil {
		temp := node

		if node.left != nil && node.left.data > temp.data {
			temp = node.left
		}
		if node.right != nil && node.right.data > temp.data {
			temp = node.right
		}

		if temp == node {
			break
		}

		node.data, temp.data = temp.data, node.data
		node = temp
	}
}

func (h *TreeHeap) Delete() (int, error) {
	if h.size == 0 {
		return 0, fmt.Errorf("Empty Heap")
	}

	removedNode := h.root.data

	if h.size == 1 {
		h.root = nil
		h.size = 0
		return removedNode, nil
	}

	lastNode := h.getLastNode()
	h.root.data = lastNode.data

	detachNode(lastNode)
	h.size -= 1

	bubbleDown(h.root)
	return removedNode, nil
}

func (h *TreeHeap) String() {
	if h.root == nil {
		fmt.Println("Empty Heap")
	}

	q := []*TreeNode{h.root}
	var result []string

	for len(q) > 0 {
		levelSize := len(q)
		var level []string

		for i := 0; i < levelSize; i++ {
			node := q[0]
			q = q[1:] // dequeue

			level = append(level, fmt.Sprintf("%v", node.data))

			if node.left != nil {
				q = append(q, node.left)
			}
			if node.right != nil {
				q = append(q, node.right)
			}
		}

		result = append(result, strings.Join(level, " "))
	}

	fmt.Println(strings.Join(result, "\n"))
}

func main() {
	h := NewTreeHeap()
	h.Insert(10)
	h.Insert(6)
	h.Insert(5)
	h.Insert(15)
	h.Insert(7)
	h.Insert(4)
	h.Insert(10)
	h.Insert(1)
	h.Insert(0)
	h.String()
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
	h.String()
}
