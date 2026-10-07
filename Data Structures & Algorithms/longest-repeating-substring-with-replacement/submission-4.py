class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_counter = [0] * 26
        most_freq = 0
        left = 0

        for right in range(len(s)):
            right_idx = ord(s[right]) - ord('A')
            window_counter[right_idx] += 1

            if window_counter[right_idx] > most_freq:
                most_freq = window_counter[right_idx]

            if (right - left + 1) - most_freq > k:
                window_counter[ord(s[left]) - ord('A')] -= 1
                left += 1

        return len(s) - left