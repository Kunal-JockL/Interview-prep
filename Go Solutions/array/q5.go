package array

func MaxSubArrayProd(n []int) []int {
	if len(n) == 0 {
		return []int{0}
	}

	var start, tempStart, end, maxSum, currentSum int = 0, 0, 0, -99999, 1

	for i, val := range n {
		currentSum *= val

		if currentSum > maxSum {
			end = i
			maxSum = currentSum
			start = tempStart
		}

		if currentSum < 0 {
			currentSum = 0
			tempStart = i + 1
		}
	}

	return n[start : end+1]
}
