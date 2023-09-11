// https://leetcode.com/problems/determine-color-of-a-chessboard-square

class Solution {
public:
    bool squareIsWhite(string coordinates) {
        return (coordinates[0]-'a'+coordinates[1])%2 != 1? true:false;
    }
};