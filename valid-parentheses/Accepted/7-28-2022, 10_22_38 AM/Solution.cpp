// https://leetcode.com/problems/valid-parentheses

class Solution {
public:
    bool isValid(string s) {
        stack<char> q;
        char p;
        for (char c:s){
            if (c == '{' || c =='[' || c == '(') q.push(c);
            else {
                if (q.empty()) return 0;
                p = q.top(); q.pop();
                if ((p == '{' && c != '}') || (p == '[' && c != ']') || (p == '(' && c != ')')) return 0;
            }
        }
        return q.empty();
    }
};