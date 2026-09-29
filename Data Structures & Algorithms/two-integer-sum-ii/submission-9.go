func twoSum(numbers []int, target int) []int {
    left, right := 0, len(numbers) - 1

    for left < right {
        curSum := numbers[left] + numbers[right]
        if curSum == target {
            return []int{left+1, right+1}
        }

        if curSum < target {
            left++
            continue
        }

        right--
    }

    return nil
}
