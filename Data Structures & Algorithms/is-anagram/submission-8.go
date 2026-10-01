func isAnagram(s string, t string) bool {
	if len(s) != len(t){
		return false
	}
	cMap := make(map[rune]int)
	for _,char:= range s{
		cMap[char]++; 
	}

	for _, char:= range t{
		cMap[char]--;

		if cMap[char] < 0{
			return false
		}
	}

	return true

}