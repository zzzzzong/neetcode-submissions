func maxArea(heights []int) int {
    ans := 0
    left, right := 0, len(heights) - 1

    for left < right {
        var h int
        if heights[left] < heights[right] {
            h = heights[left]
        } else {
            h = heights[right]
        }

        water := h * (right - left)
        if ans < water {
            ans = water
        }

        if heights[left] == heights[right] {
            left++
            for left < right && heights[left] <= h {
                left++
            }
            right--
            for left < right && heights[right] <= h {
                right--
            }
            continue
        }

        if h == heights[left] {
            left++
            for left < right && heights[left] <= h {
                left++
            }
            continue
        }

        right--
        for left < right && heights[right] <= h {
            right--
        }
    }
    
    return ans
}
