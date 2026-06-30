class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # 存 index
        max_area = 0
        
        heights.append(0) # dummy bar
        
        for i in range(len(heights)):
            # current bar 比 stack top矮，觸發結算
            while stack and heights[i] < heights[stack[-1]]:
                mid_index = stack.pop()
                the_height = heights[mid_index]
                # 如果 stack 空了，代表左邊界是起點；否則左邊界就是新的 stack 頂端
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, the_height * width)
                
            stack.append(i)
            
        return max_area