// https://leetcode.com/problems/subdomain-visit-count

class Solution:
    
    def insert(self, count, domain):
        split_domain = domain.split('.')
        for i in range(len(split_domain)):
            subdomain = '.'.join(split_domain[i:])
            if not subdomain in self.m:
                self.m[subdomain] = int(count)
            else:
                self.m[subdomain] += int(count)
    
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        self.m = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            self.insert(count, domain)
        
        return [str(self.m[k]) + ' ' + k for k in self.m]