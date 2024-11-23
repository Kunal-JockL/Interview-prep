package array

import "math"

func MaxSubArray2(ar []int) []int {
	var m, mi, mj int = -99999, -1, -1
	for i := 0; i < len(ar); i++ {
		for j := i + 1; j < len(ar); j++ {
			if Sum(ar[i:j]) > m {
				mi, mj = i, j
				m = Sum(ar[i:j])
			}
		}
	}
	return ar[mi:mj]
}

func Sum(arr []int) int {
	sum := 0
	for _, value := range arr {
		sum += value
	}
	return sum
}

func MaxSubArray(arr []int) []int {
	if len(arr) == 0 {
		return []int{}
	}

	maxSum := math.MinInt32
	currentSum := 0
	start, end, tempStart := 0, 0, 0

	for i, value := range arr {
		currentSum += value

		// Update maxSum and subarray indices if currentSum is greater than maxSum
		if currentSum > maxSum {
			maxSum = currentSum
			start = tempStart
			end = i
		}

		// Reset currentSum if it drops below zero
		if currentSum < 0 {
			currentSum = 0
			tempStart = i + 1
		}
	}

	return arr[start : end+1]
}
