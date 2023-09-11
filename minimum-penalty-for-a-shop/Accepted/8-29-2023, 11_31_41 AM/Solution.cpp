// https://leetcode.com/problems/minimum-penalty-for-a-shop

class Solution {
public:
    int bestClosingTime(string customers) {
        int curP = 0, minP = 0, minH = 0;
        for (int i = 1; i <= customers.size(); ++i) {
            if (customers[i-1] == 'Y') --curP;
            else ++curP;
            if (curP < minP) {
                minP = curP;
                minH = i;
            }
        }
        return minH;
    }
};