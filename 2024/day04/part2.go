package main

import (
	"bufio"
	"fmt"
	"os"
)

// Define offsets for X-MAS pattern
var xmasOffsets = [4][2]int{
	{-1, -1}, // Top-left MAS
	{1, -1},  // Bottom-left MAS
	{-1, 1},  // Top-right MAS
	{1, 1},   // Bottom-right MAS
}

func countXMAS(grid []string) int {
	height := len(grid)
	if height == 0 {
		return 0
	}

	width := len(grid[0])
	count := 0

	for y := 1; y < height-1; y++ {
		for x := 1; x < width-1; x++ {
			// Check if the center is 'A'
			if grid[y][x] != 'A' {
				continue
			}

			// Check each diagonal pair
			foundXMAS := 0
			for _, offset := range xmasOffsets {
				dx, dy := offset[0], offset[1]
				nx, ny := x+dx, y+dy
				ox, oy := x-dx, y-dy

				// Ensure bounds and validate 'M' and 'S' pairing
				if ny >= 0 && ny < height && nx >= 0 && nx < width &&
					oy >= 0 && oy < height && ox >= 0 && ox < width &&
					((grid[ny][nx] == 'M' && grid[oy][ox] == 'S') || (grid[ny][nx] == 'S' && grid[oy][ox] == 'M')) {
					foundXMAS++
				}
			}

			// A valid X-MAS requires exactly 4 diagonal pairs
			if foundXMAS == 4 {
				count++
			}
		}
	}

	return count
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	var grid []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if len(line) > 0 {
			grid = append(grid, line)
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	if len(grid) == 0 {
		fmt.Println("Grid is empty.")
		return
	}

	result := countXMAS(grid)
	fmt.Println("Result:", result)
}
