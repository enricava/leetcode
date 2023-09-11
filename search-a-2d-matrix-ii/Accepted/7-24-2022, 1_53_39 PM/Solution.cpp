// https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        
        int r = rows-1;
        int c = 0;
        
        while (r >= 0 and c < cols){
            if (matrix[r][c] > target) r--;
            else if (matrix[r][c] < target) c++;
            else return 1;
        }
        return 0;
    }
};