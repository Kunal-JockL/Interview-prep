package strings

func ReverseUsingRecursion(s []rune, i int, j int) string {
	if i >= j {
		return string(s)
	}
	s[i], s[j] = s[j], s[i]
	return ReverseUsingRecursion(s, i+1, j-1)
}
