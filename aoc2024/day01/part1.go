package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

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

	sort.Slice(list1, func(i, j int) bool { return list1[i] < list1[j] })
	sort.Slice(list2, func(i, j int) bool { return list2[i] < list2[j] })

	result := 0

	for i := 0; i < len(list1); i++ {
		if list1[i] > list2[i] {
			tmp := uint(int(list1[i] - list2[i]))
			result += int(tmp)
		} else {
			tmp := uint(int(list2[i] - list1[i]))
			result += int(tmp)
		}
	}
	println("Result:", result)
}
