// https://leetcode.com/problems/valid-anagram

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return 0;
        vector<int> v(26,0);
        for (int i = 0; i < s.size(); ++i){
            v[s[i]-'a']++;
            v[t[i]-'a']--;
        }
        for (int val:v) if (val) return 0;
        return 1;
    }
};