// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution {
public:
    
    int lengthOfLongestSubstring(string s) {
        int n = s.size();
        int count = 0, m = 0;
        unordered_set<char> set;
        for(int i = 0; i < n; ++i){
            if(set.count(s[i])){
                m = max(count, m);
                count = 0;
                set.empty();
            }
            count++;
            set.insert(s[i]);
        }
        return m;
    }
};