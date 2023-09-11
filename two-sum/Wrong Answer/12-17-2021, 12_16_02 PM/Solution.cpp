// https://leetcode.com/problems/two-sum

class Solution {
public:
    
    int sum(vector<int> & nums, int i, int j){
        return nums[i] + nums[j];
    }
    
    vector<int> twoSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int i = 0, j = nums.size()-1;
        int s = sum(nums, i,j);
        while (s != target){
            if(s > target) --j;
            else ++i;
            s = sum(nums,i,j);
        }
        return {i,j};
    }
};