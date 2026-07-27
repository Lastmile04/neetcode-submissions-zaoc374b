func fourSum(nums []int, target int) [][]int {
    var result [][]int
    n := len(nums)

    if n < 4 {
        return result
    }

    sort.Ints(nums)

    for i := 0; i < n-3; i++ {

        if i > 0 && nums[i] == nums[i-1] {
            continue
        }

        if nums[i]+nums[i+1]+nums[i+2]+nums[i+3] > target {
            break
        }

        if nums[i]+nums[n-3]+nums[n-2]+nums[n-1] < target {
            continue
        }

        for j := i + 1; j < n-2; j++ {

            if j > i+1 && nums[j] == nums[j-1] {
                continue
            }


            if nums[i]+nums[j]+nums[j+1]+nums[j+2] > target {
                break
            }

            if nums[i]+nums[j]+nums[n-2]+nums[n-1] < target {
                continue
            }

            l, r := j+1, n-1

            for l < r {
                sum := nums[i] + nums[j] + nums[l] + nums[r]

                if sum == target {
                    result = append(result, []int{nums[i], nums[j], nums[l], nums[r]})

                    for l < r && nums[l] == nums[l+1] {
                        l++
                    }
                    for l < r && nums[r] == nums[r-1] {
                        r--
                    }

                    l++
                    r--
                } else if sum < target {
                    l++
                } else {
                    r--
                }
            }
        }
    }

    return result
}