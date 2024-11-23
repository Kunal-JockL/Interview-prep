package strings

func CleanBrackets(s string) string {
	rs := []rune(s)
	bracs := []rune("()")
	str := ""

	for i := 0; i < len(rs)-1; i++ {
		if rs[i] == bracs[0] && rs[i+1] == bracs[1] {
			str += "()"
		}
	}
	return str
}
