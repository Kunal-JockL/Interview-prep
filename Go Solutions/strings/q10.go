package strings

func Palindrome(s string) bool {
	rs := []rune(s)
	var b bool = true
	for i, j := 0, len(rs)-1; i < j; i, j = i+1, j-1 {
		if rs[i] != rs[j] {
			b = false
		}
	}
	return b
}
