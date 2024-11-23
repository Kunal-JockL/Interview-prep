package strings

func RBY(s string) string {
	char := []rune("rby")
	sr := []rune(s)
	r, b, y := char[0], char[1], char[2]
	i, k := 0, len(sr)-1
	for sr[i] == r {
		i++
	}
	j := i
	for j <= k {
		for sr[i] == r {
			i++
		}
		for sr[k] == y {
			k--
		}
		for sr[j] == b {
			j++
		}
		if sr[j] == r {
			sr[i], sr[j] = sr[j], sr[i]
			i++
			j++
		} else {
			sr[j], sr[k] = sr[k], sr[j]
			j++
			k--
		}
	}
	return string(sr)
}
