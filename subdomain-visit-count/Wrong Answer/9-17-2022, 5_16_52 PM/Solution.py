// https://leetcode.com/problems/subdomain-visit-count

class Solution:
    
    def insert(self, count, domain):
        split_domain = domain.split('.')
        for i in range(len(split_domain)):
            subdomain = '.'.join(split_domain[i:])
            if subdomain in self.m:
                self.m[subdomain] += count
            else:
                self.m[subdomain] = count
    
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        self.m = {}
        for cpdomain in cpdomains:
            cp = cpdomain.split()
            count = cp[0]
            domain = cp[1]
            self.insert(count, domain)
        
        return [str(self.m[k]) + ' ' + k for k in self.m]