func isPalindrome(s string) bool {
	left := 0
	right := len(s)-1
	
	for left < right{
		for left < right && !isAlphaNum(rune(s[left])){
			left++
		}

		for right > left && !isAlphaNum(rune(s[right])){
			right--
		}

		if unicode.ToLower(rune(s[left])) != unicode.ToLower(rune(s[right])){
			return false
		}
		left++
		right--
	}
	return true
}

func isAlphaNum(c rune) bool{
	return unicode.IsLetter(c) || unicode.IsDigit(c)
}
