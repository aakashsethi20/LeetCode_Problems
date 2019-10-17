"""
Submission: Accepted!

Runtime: 132 ms, faster than 97.11% of Python3 online submissions for Container With Most Water.
Memory Usage: 15.3 MB, less than 5.26% of Python3 online submissions for Container With Most Water.
"""

class Solution:

    def maxArea(self, height: [int]) -> int:
        max_area = left = 0
        right = len(height) - 1
        while left < right:
            left_element = height[left]
            right_element = height[right]

            current_area = min(left_element, right_element) * (right - left)
            if current_area > max_area:
                max_area = current_area

            if left_element < right_element:
                while left < right and height[left] <= left_element:
                    left = left + 1
            else:
                while right > left and height[right] <= right_element:
                    right = right - 1

        return max_area

def main():
    heights = [1,8,6,2,5,4,8,3,7]

    solution = Solution()

    print(solution.maxArea(heights))

if __name__ == "__main__":
    main()
