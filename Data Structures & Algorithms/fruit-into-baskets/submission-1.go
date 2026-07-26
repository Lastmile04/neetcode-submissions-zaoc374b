func totalFruit(fruits []int) int {
	fMap := make(map[int]int)
	maxFruits := 0
	l := 0
	for r, rVal := range(fruits){
		fMap[rVal]++
		for len(fMap) > 2{
			val  := fMap[fruits[l]]
			if val == 1{
				delete(fMap, fruits[l])
			} else{
				fMap[fruits[l]]--
			}
			l++
		}
		maxFruits = max(maxFruits, r-l+1)
	}
	return maxFruits
}
