/*
 The following code runs in 6ms and is at 98.42 percentile of all cpp submissions at LeetCode
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        unordered_map<int, int> map;
        vector<int> answer;
        
        for (int i=0; i < nums.size(); i++)
        {
            int toFind = target - nums[i];
            
            if (map.find(toFind) != map.end())
            {
                answer.push_back(map[toFind]);
                answer.push_back(i);
                return answer;
            }
            map[nums[i]] = i;
        }
    }
};