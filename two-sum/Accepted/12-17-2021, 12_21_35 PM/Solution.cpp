// https://leetcode.com/problems/two-sum

class Solution {
public:
    
    int sum(vector<int> & nums, int i, int j){
        return nums[i] + nums[j];
    }
    
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> sol; bool found = 0;
        for(int i = 0; i < nums.size()-1 && !found;++i){
            for(int j = nums.size()-1; j > i && !found; --j){
                if(sum(nums, i,j) == target) {
                    sol = {i,j};
                    found = 1;
                }
            }
        }
        return sol;
    }
};