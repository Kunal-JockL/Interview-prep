package array

import "fmt"

func SortArr(ar []int) []int {
	var c, z, t int = 0, 0, len(ar) - 1
	for c <= t {
		fmt.Printf("c:%v z:%v t:%v\n", c, z, t)
		if ar[c] == 0 {
			ar[c], ar[z] = ar[z], ar[c]
			z++
			c++
		} else if ar[c] == 2 {
			ar[c], ar[t] = ar[t], ar[c]
			t--

		} else {
			c++
		}
		fmt.Printf("%v\n", ar)
	}
	return ar
}
