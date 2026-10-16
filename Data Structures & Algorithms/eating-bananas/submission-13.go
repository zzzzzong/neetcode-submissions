func minEatingSpeed(piles []int, h int) int {
	left := 1
	right := 0
	for _, val := range piles {
		if val > right {
			right = val
		}
	}



	for left < right {
		mid := left + (right - left) / 2

		time := 0
		for _, p := range piles {
			time += (p + mid - 1) / mid
		}

		if time > h {
			left = mid + 1
			continue
		}
		right = mid

	}
	

	return left
}
