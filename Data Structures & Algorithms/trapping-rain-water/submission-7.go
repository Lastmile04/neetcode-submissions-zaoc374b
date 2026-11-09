func trap(height []int) int {
	if len(height) == 0{
		return 0
	}

	l, r := 0, len(height)-1
    maxL, maxR := height[l], height[r]
    ttl := 0

 	for l<r{
		if maxL<maxR {
			l++
			maxL = max(maxL, height[l])
			ttl += maxL - height[l]
		}else{
			r--
			maxR = max(maxR, height[r])
			ttl += maxR - height[r]
		}
 	}
	return ttl
}

func max(a,b int) int{
	if a>b{
		return a
	}
	return b
}