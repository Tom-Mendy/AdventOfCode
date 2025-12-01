package main

import (
	"bufio"
	"fmt"
	"os"
)

var directions = [8][2]int{
	{0, 1},   // right
	{1, 0},   // down
	{1, 1},   // diagonal down-right
	{-1, 1},  // diagonal up-right
	{0, -1},  // left
	{-1, 0},  // up
	{-1, -1}, // diagonal up-left
	{1, -1},  // diagonal down-left
}

func countOccurrences(grid []string, word string) int {
	height := len(grid)
	if height == 0 {
		return 0
	}

	width := len(grid[0])
	wordLength := len(word)
	count := 0

	for y := 0; y < height; y++ {
		for x := 0; x < width; x++ {
			// Check all directions
			for _, dir := range directions {
				dx, dy := dir[0], dir[1]
				found := true

				// Check each character of the word
				for i := 0; i < wordLength; i++ {
					nx, ny := x+i*dx, y+i*dy

					// If out of bounds or character mismatch, stop
					if nx < 0 || ny < 0 || nx >= width || ny >= height || grid[ny][nx] != word[i] {
						found = false
						break
					}
				}

				if found {
					count++
				}
			}
		}
	}

	return count
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()

	result := 0
	text := "XMAS"
	tab := []string{}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if len(line) > 0 {
			tab = append(tab, line)
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	if len(tab) == 0 {
		fmt.Println("Grid is empty.")
		return
	}

	result = countOccurrences(tab, text)
	fmt.Println("Result:", result)
}
