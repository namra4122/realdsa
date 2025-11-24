package main

import "fmt"

type Edges struct {
	start  int
	end    int
	weight int
}

func CreateAdjMatrix(nodes int, edges []Edges) {
	graph := make([][]int, nodes)

	for i := range nodes {
		graph[i] = make([]int, nodes)
	}

	for _,e := range edges{
		graph[e.start][e.end] = e.weight
		// graph[e.end][e.start] = e.weight // uncomment if you want the graph to be undirected
	}

	for _,g := range graph{
		fmt.Println(g)
	}
}

func main() {
	nodes := 4
	edges := []Edges{
		{0, 1, 5},
		{0, 2, 3},
		{1, 2, 2},
		{2, 0, 1},
		{2, 3, 4},
		{3, 3, 7},
	}
	// direacted graph
	CreateAdjMatrix(nodes, edges)
}
