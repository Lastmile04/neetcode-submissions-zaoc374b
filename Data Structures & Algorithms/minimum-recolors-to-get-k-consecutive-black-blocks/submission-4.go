func minimumRecolors(blocks string, k int) int {
	l := 0
	minCount := math.MaxInt
	count := 0
	for r:= 0; r<len(blocks); r++{
		if blocks[r] == 'W'{count++}
		if r-l+1 == k{
			minCount = min(minCount, count)
			if blocks[l] == 'W'{count--}
			l++
		}
	}
	return minCount
}