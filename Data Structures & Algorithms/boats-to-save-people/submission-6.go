import "slices"
func numRescueBoats(people []int, limit int) int {
	slices.Sort(people)
	l := 0
	r := len(people) - 1
	boats := 0
	for l <= r {
		if people[l]+people[r] <= limit {
			l++
		}

		r--
		boats++
	}
	return boats
}