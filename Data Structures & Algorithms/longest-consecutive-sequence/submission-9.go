type Set[T comparable]struct{
	elements map[T]struct{}
}

func NewSet[T comparable]() *Set[T]{
	return &Set[T]{
		elements: make(map[T]struct{}),
	}
}

func (s *Set[T]) Add(value T){
	if s.Contains(value){
		return
	}
	s.elements[value] = struct{}{}
}

func (s *Set[T]) Contains(value T)bool{
	_,exists := s.elements[value]
	return exists
}

func longestConsecutive(nums []int) int {
	if len(nums) == 0{
		return 0
	}

	set := NewSet[int]()

	for i:= range nums{
		set.Add(nums[i])
	}

	longestStreak := 0

	for _, num := range nums{
		if !set.Contains(num-1){
			currentNum := num
			currentStreak := 1

			for set.Contains(currentNum + 1){
				currentNum++
				currentStreak++
			}

			if currentStreak > longestStreak{
				longestStreak = currentStreak
			}
		}
	}
	return longestStreak
}
