func lengthOfLongestSubstring(s string) int {
    length := 0
    l := 0
    // Using a 256-element array to track the last seen index of each ASCII byte
    lastSeen := [256]int{}
    for i := range lastSeen {
        lastSeen[i] = -1
    }

    for r := 0; r < len(s); r++ {
        char := s[r]
        if lastSeen[char] >= l {
            l = lastSeen[char] + 1
        }
        length = max(length, r - l + 1)
        lastSeen[char] = r
    }
    return length
}