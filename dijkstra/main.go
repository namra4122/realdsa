package main

import "fmt"

type Edge struct {
	Node   int
	Weight int
}

func FindPath(start int, end int, adjList [][]Edge) (int, string) {
	return 0, "Tere pass koi rasta nahi hai"
}

func main() {
	adjList := [][]Edge{
		{{1, 4}, {2, 8}},
		{{0, 4}, {4, 6}},
		{{0, 8}, {3, 2}},
		{{2, 2}, {4, 10}},
		{{1, 6}, {3, 10}},
	}

	dist, path := FindPath(0,0, adjList)
	fmt.Printf("Distance: %d\n", dist)
	fmt.Printf("Path: %s\n", path)
}
