type Solution struct{}

func (s *Solution) Encode(strs []string) string {
	encoded:=make([]string, len(strs))
	for i,str:=range strs{
		encoded[i] = fmt.Sprintf("%d:%s", len(str), str)
	}
	return strings.Join(encoded, "")
}

func (s *Solution) Decode(encoded string) []string {
	offset := 0
	strLen := len(encoded)
	var res []string

	for offset<strLen {
		length := 0

		for offset<strLen && encoded[offset] != ':' { // read length first
			length = length * 10 +  int(encoded[offset] - '0')
			offset++
		}
		offset++ // de-limiter skip
		res = append(res,encoded[offset:offset+length])
		offset+=length
	}
	return res
}
