// https://leetcode.com/problems/two-sum

class Solution {
public:
    
    int sum(vector<pair<int,int>> & v, int i, int j){
        return v[i].first + v[j].first;
    }
    
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        vector<pair<int,int>> v(n);
        for(int i = 0; i < n; ++i){
            v[i] = {nums[i],i};
        }
        sort(v.begin(), v.end());
        int i = 0, j = n-1;
        int s = sum(v, i,j);
        while (s != target){
            if(s < target) ++i;
            else --j;
            s = sum(v,i,j);
        }
        return {v[i].second,v[j].second};
    }
};