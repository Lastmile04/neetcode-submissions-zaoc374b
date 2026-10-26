func characterReplacement(s string, k int) int {
	count := make(map[byte]int)
	res, l, maxf := 0, 0, 0
	
	for r:=0; r< len(s); r++{
		// update the distinct element frequency
		count[s[r]]++
		// update maxf if possible
		if count[s[r]] > maxf{
			maxf = count[s[r]]
		}

		// shirk window until it becomes valid
		for r-l+1 - maxf > k {
			count[s[l]]--
			l++
		}

		// update the result if the current window exceed current max size
		if r-l+1 > res{
			res = r-l+1
		}
	} 
	return res
}
