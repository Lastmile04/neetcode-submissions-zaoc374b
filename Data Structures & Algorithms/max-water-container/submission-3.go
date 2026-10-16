func maxArea(heights []int) int {
    l := 0
    r := len(heights) - 1
    maxWater := 0

    for l < r {
        // Calculate the area with the current boundaries
        currentArea := (r - l) * min(heights[l], heights[r])
        if currentArea > maxWater {
            maxWater = currentArea
        }

        // Move the pointer pointing to the shorter line inward
        if heights[l] < heights[r] {
            l++
        } else {
            r--
        }
    }

    return maxWater
}
