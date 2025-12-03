package main

import "fmt"

type Node struct {
	data int
	next *Node
}

type SinglyLL struct {
	head *Node
}

func NewSinglyLL() *SinglyLL {
	return &SinglyLL{}

}

func (sll *SinglyLL) AddNode(value int) {
	new_node := Node{
		data: value,
		next: nil,
	}

	if sll.head == nil {
		sll.head = &new_node
		return
	}

	curr := sll.head
	for curr.next != nil {
		curr = curr.next
	}

	curr.next = &new_node
	return
}

func (sll *SinglyLL) Insert(index int, value int) {
	new_node := Node{
		data: value,
		next: nil,
	}

	if index == 0 {
		new_node.next = sll.head
		sll.head = &new_node
		return
	}

	curr_idex := 0
	curr := sll.head
	for curr != nil && curr_idex < index-1 {
		curr = curr.next
		curr_idex += 1
	}

	if curr == nil {
		fmt.Printf("%dth exist nahi karta sirji\n", index)
	}

	new_node.next = curr.next
	curr.next = &new_node
	return
}

func (sll *SinglyLL) Remove(index int) {
	curr := sll.head
	curr_idex := 0

	for curr_idex != index-1 {
		if curr.next != nil {
			curr = curr.next
			curr_idex += 1
		} else {
			fmt.Printf("linkedlist ka size hi %d etna hai kaise %dth pr remove kareji mai??", curr_idex+1, index)
		}
	}

	curr.next = curr.next.next
	return
}

func (sll *SinglyLL) Pop() (int, error) {
	if sll.head == nil {
		return 0, fmt.Errorf("Linked list to empty hai boss!!")
	}

	if sll.head.next == nil {
		data := sll.head.data
		sll.head = nil
		return data, nil
	}

	curr := sll.head
	for curr.next.next != nil {
		curr = curr.next
	}

	data := curr.next.data
	curr.next = nil
	return data, nil
}

func (sll *SinglyLL) Get(index int) (int, error) {
	if sll.head == nil {
		return 0, fmt.Errorf("List to empty hai boss!!")
	}
	curr_idex := 0
	curr := sll.head

	for curr != nil && curr_idex < index {
		curr = curr.next
		curr_idex += 1
	}

	if curr == nil {
		return 0, fmt.Errorf("%dth index hi exist nhi karta!!", index)
	}
	return curr.data, nil
}

func (sll *SinglyLL) Search(data int) (string, error) {
	curr_idex := 0
	curr := sll.head
	for curr != nil && curr.data != data {
		curr_idex += 1
		curr = curr.next
	}

	if curr == nil {
		return "", fmt.Errorf("koi node nahi hai with data: %d", data)
	}

	return fmt.Sprintf("yeh lo index: %d aur uski value:%d", curr_idex, curr.data), nil
}

func (sll *SinglyLL) Print() {
	curr := sll.head
	for curr != nil {
		fmt.Printf("%d -> ", curr.data)
		curr = curr.next
	}
	fmt.Println("nil")
}

func main() {
	sll := NewSinglyLL()
	sll.AddNode(5)
	sll.AddNode(5)
	sll.AddNode(3)
	sll.AddNode(1)
	sll.AddNode(2)
	sll.AddNode(3)
	sll.AddNode(1)
	sll.AddNode(2)
	sll.Insert(1, 4)
	sll.Remove(1)
	val, err := sll.Pop()
	if err != nil {
		panic(err)
	}
	fmt.Printf("Pop Value: %d\n", val)
	val1, err := sll.Get(1)
	if err != nil {
		panic(err)
	}
	fmt.Printf("Get Value: %d\n", val1)
	val2, err := sll.Search(3)
	if err != nil {
		panic(err)
	}
	fmt.Printf("%s\n", val2)
	sll.Print()
}
