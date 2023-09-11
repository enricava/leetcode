// https://leetcode.com/problems/two-sum

use std::collections::HashMap;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut comp : HashMap<i32, i32> = HashMap::new();
        for (i, num) in nums.iter().enumerate() {
            match comp.get(num){
                Some(&index) => return vec![index, i as i32],
                None => comp.insert(target - num, i as i32)
            };
        }
        vec![]
    }
}