package array

func SL(n int, arr []int) int {
	var m, lm int = 0, 0
	for i := 0; i < n; i++ {
		if arr[i] > m {
			lm = m
			m = arr[i]
		}
	}
	return lm
}
