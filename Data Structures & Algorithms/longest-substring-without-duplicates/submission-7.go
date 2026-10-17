type Set[T comparable] struct{
	elements map[T]struct{}
}

func NewSet[T comparable]() *Set[T]{
	return &Set[T]{
		elements: make(map[T]struct{}),
	}
}

func (s *Set[T]) Add(value T){
	if _, exists := s.elements[value]; exists{
		return
	}
	s.elements[value] = struct{}{}
}

func (s *Set[T]) Contains(value T)bool{
	_, exists:= s.elements[value]
	return exists
}

func (s *Set[T]) Remove(value T){
	delete(s.elements,value)
}

func lengthOfLongestSubstring(s string) int {
	length:= 0
	l:=0
	r:=0
	set := NewSet[byte]()
	for r<=len(s)-1{
		if set.Contains(s[r]) == true{
			for set.Contains(s[r]) == true{	
				set.Remove(s[l])
				l++
			}
		}
		length = max(length, r-l+1)
		set.Add(s[r])
		r++
	}
	return length
}
