// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {  
        int n = nums.size();
        if (n == 1) return 1;
        int k = 0, j = 1;
        while (k < n){
            while (j < n && nums[k]==nums[j])j++;
            if (j == n) return k + 1;
            nums[k+1] = nums[j];
            k++;
        }
        return k + 1;
    }
};