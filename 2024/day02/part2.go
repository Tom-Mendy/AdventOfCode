package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func increase(list []int) bool {
	for i := 0; i < len(list)-1; i++ { // Iterate up to len(list)-1
		if !(list[i] < list[i+1] && list[i]+3 >= list[i+1]) {
			return false
		}
	}
	return true
}

func decrease(list []int) bool {
	for i := 0; i < len(list)-1; i++ { // Iterate up to len(list)-1
		if !(list[i] > list[i+1] && list[i]-3 <= list[i+1]) {
			return false
		}
	}
	return true
}

func generate_all_possibility(list []int) [][]int {
	var result [][]int
	for i := 0; i < len(list); i++ {
		tmp := append([]int{}, list[:i]...)
		tmp = append(tmp, list[i+1:]...)
		result = append(result, tmp)
	}
	return result
}

func safe(list []int) bool {

	if increase(list) {
		return true
	} else if decrease(list) {
		return true
	}
	all_possibility := generate_all_possibility(list)
	fmt.Printf("All possibility: %+v\n", all_possibility)
	for _, v := range all_possibility {
		if increase(v) {
			return true
		} else if decrease(v) {
			return true
		}
	}
	return false
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer file.Close()

	result := 0
	int_level := []int{}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		splitLine := strings.Split(scanner.Text(), " ")
		if len(splitLine) >= 2 {
			int_level = []int{}
			for _, v := range splitLine {
				int_value, err := strconv.Atoi(v)
				if err != nil {
					fmt.Println(err)
					continue
				}
				int_level = append(int_level, int_value)

			}

			if safe(int_level) {
				result += 1
			}
		}

	}

	println("Result:", result)
}
