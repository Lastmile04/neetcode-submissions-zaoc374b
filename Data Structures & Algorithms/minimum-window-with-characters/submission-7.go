func minWindow(s string, t string) string {
	if len(s) == 0 || len(t) == 0 || len(s) < len(t){
		return ""
	}

    var t_freq [256]int
	var sub_freq [256]int

	for i:=0; i< len(t); i++{
		t_freq[t[i]]++
	}

	minLen:= math.MaxInt32
	minL, minR := 0, 0
	req, formed:=0, 0
	
	for _, count := range t_freq{
		if count > 0{
			req++
		}
	}

	l,r := 0,0

	for r<len(s){
		r_char := s[r]
		sub_freq[r_char]++

		if t_freq[r_char] > 0 && sub_freq[r_char] == t_freq[r_char]{
			formed++
		}

		for l<=r && formed == req{
			
			if r-l+1 < minLen{
				minLen = r-l+1
				minL = l
				minR = r
			}

			l_char := s[l]
			sub_freq[l_char]--

			if t_freq[l_char] > 0 && sub_freq[l_char] < t_freq[l_char]{
				formed--
			}
			l++
		}
		r++
	}

	if minLen == math.MaxInt32{
		return ""
	}
	return s[minL:minR+1]
}
