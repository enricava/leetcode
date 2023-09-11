// https://leetcode.com/problems/the-number-of-weak-characters-in-the-game

class Solution {
public:
    bool static ord(vector<int> &a,vector<int> &b){
        if(a[0]!=b[0])
            return a[0]<b[0];
        else
            return a[1]>b[1];
    }
    int numberOfWeakCharacters(vector<vector<int>>& properties) {
        int n=properties.size();
        int count=0;
        sort(properties.begin(),properties.end(),ord);
        int m=properties[n-1][1];
        for(int i=n-2;i>=0;i--){
                if(properties[i][1]<m)
                    count++;
                m=max(m,properties[i][1]);
        }
        return count;
    }
};