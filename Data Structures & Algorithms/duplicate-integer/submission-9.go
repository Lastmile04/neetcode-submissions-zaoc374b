

type Set [T comparable] struct {
	elements map[T]struct{}
}

func NewSet [T comparable]() *Set[T]{
	return &Set[T]{
		elements: make(map[T]struct{}),
	}
}

func (s *Set[T]) Add(value T){
	if s.elements == nil{
		s.elements = make(map[T]struct{})
	}
	s.elements[value] = struct{}{}
}

func (s *Set[T]) Contains(value T) bool{
	_, found := s.elements[value]
	return found
}

func hasDuplicate(nums []int) bool {
	set := NewSet[int]()
    for _, value := range nums{
		if set.Contains(value){
			return true
		}
		set.Add(value)
	}
	return false
}
