package main

import "fmt"

type EdgeList struct {
	start int
	end int
	weight int
}

type Edges struct {
	node int
	weight int
}

func CreateAdjList(nodes int, edges []EdgeList) {
	graph := make(map[int][]Edges)

	for _, e := range edges {
		graph[e.start] = append(graph[e.start], Edges{e.end, e.weight})
		// graph[e.end] = append(graph[e.end], Edges{e.start, e.weight}) // uncomment if you want the graph to be undirected
	}

	for k,v := range graph {
		fmt.Print(k, " => ", v, "\n");
	}
}

func main(){
	nodes := 4
	edges := []EdgeList {
		{0, 1, 5},
		{0, 2, 3},
		{1, 2, 2},
		{2, 0, 1},
		{2, 3, 4},
		{3, 3, 7},
	}

	// direacted graph
	CreateAdjList(nodes, edges)
}
