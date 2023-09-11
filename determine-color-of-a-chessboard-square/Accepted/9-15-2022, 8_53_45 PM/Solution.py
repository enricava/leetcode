// https://leetcode.com/problems/determine-color-of-a-chessboard-square

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return True if (ord(coordinates[0]) - ord('a') + ord(coordinates[1]))%2 != 1 else False