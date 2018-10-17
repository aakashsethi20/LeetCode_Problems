"""
Solution takes 52 ms to run all the cases. It's faster than 99.44% of submission using Python3 on Leetcode.
"""

class Solution:

    def reverse_negative(self, x_chars):
        x_reverse = x_chars[0:1] + x_chars[:0:-1]
        x_reverse_str = ''.join(x_reverse)
        x = int(x_reverse_str)
        if -2**31 <= x < 0:
            return x
        return 0

    def reverse_positive(self, x_chars):
        x_chars.reverse()
        x_reverse_str = ''.join(x_chars)
        x = int(x_reverse_str)
        if 1 < x < 2**31:
            return x
        return 0

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        x_chars = list(str(x))

        if x > 0:
            return self.reverse_positive(x_chars)
        else:
            return self.reverse_negative(x_chars)
        return 0
