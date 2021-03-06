'''
A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the
coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its
top-right corner.

Two rectangles overlap if the area of their intersection is positive.  To be
clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

Example 1:
Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true

Example 2:
Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false

Notes:
Both rectangles rec1 and rec2 are lists of 4 integers.
All coordinates in rectangles will be between -10^9 and 10^9.
'''

from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        l1 = rec1[2] - rec1[0]
        l2 = rec2[2] - rec2[0]
        h1 = rec1[3] - rec1[1]
        h2 = rec2[3] - rec2[1]
        lengh = max(abs(rec2[2] - rec1[0]), abs(rec1[2] - rec2[0]))
        height = max(abs(rec2[3] - rec1[1]), abs(rec1[3] - rec2[1]))
        return lengh < (l1 + l2) and height < (h1 + h2)


if __name__ == '__main__':
    a = Solution()
    print(a.isRectangleOverlap([5, 15, 8, 18], [0, 3, 7, 9]))
