package main

import (
	"io/fs"
	"log"
	"path/filepath"
)

func main() {
	root := "data"

	err := filepath.WalkDir(root, func(path string, d fs.DirEntry, err error) error {
		if err != nil {
			return err
		}

		// // Skip directories
		// if d.IsDir() {
		// 	return nil
		// }

		// // Only read .txt files
		// if filepath.Ext(path) == ".txt" {
		// 	_, err := ioutil.ReadFile(path)
		// 	if err != nil {
		// 		return err
		// 	}

		// 	fmt.Printf("---- %s ----\n", d)
		// }

		return nil
	})

	if err != nil {
		log.Fatal(err)
	}
}
