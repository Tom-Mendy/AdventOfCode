package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func counter(list []uint64, value uint64) int {
	counter := 0
	for _, v := range list {
		if v == value {
			counter++
		}
	}
	return counter
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer file.Close()

	list1 := []uint64{}
	list2 := []uint64{}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		splitLine := strings.Split(scanner.Text(), "   ")

		value, err := strconv.ParseUint(splitLine[0], 10, 64)
		if err != nil {
			fmt.Println(err)
			continue
		}
		list1 = append(list1, value)
		value, err = strconv.ParseUint(splitLine[1], 10, 64)
		if err != nil {
			fmt.Println(err)
			continue
		}
		list2 = append(list2, value)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}

	result := 0

	for i := 0; i < len(list1); i++ {

		result += int(list1[i]) * counter(list2, list1[i])
	}
	println("Result:", result)
}
