// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution {
public:
    
    int lengthOfLongestSubstring(string s) {
        int n = s.size();
        unordered_map<char,int> set;
        int m = 0;
        int i = 0;
        for(int j = 0; j < n; ++j){
            if(set.count(s[j])){
                i = max(i, set[s[j] +1]);
            }
            set[s[j]] = j;
            m = max(m, j-i);
        }
        return m;
    }
};