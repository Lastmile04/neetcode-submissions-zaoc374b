func characterReplacement(s string, k int) int {
	freq := make(map[byte]int)
	res, l, maxFreq := 0, 0, 0

	for r:= 0; r < len(s); r++{
		freq[s[r]]++;

		if freq[s[r]] > maxFreq{
			maxFreq = freq[s[r]]
		}

		for r-l+1 - maxFreq > k{
			freq[s[l]]--
			l++
		}

		if r-l+1 > res{
			res = r-l+1
		}
	}

	return res
}
