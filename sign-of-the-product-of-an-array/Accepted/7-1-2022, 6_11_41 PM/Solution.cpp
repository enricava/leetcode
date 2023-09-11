// https://leetcode.com/problems/sign-of-the-product-of-an-array

class Solution {
public:
    int arraySign(vector<int>& nums) {
        bool neg = 0;
        for (int n:nums){
            if (n==0) return 0;
            else if (n<0) neg = !neg;
        }
        return (neg)? -1:  1;
    }
};