#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> pos_map;
        for (int i = 0; i < nums.size(); i++) {
            pos_map[nums[i]] = i;
        }
        for (int j = 0; j < nums.size(); j++) {
            int complement = target - nums[j];
            if (auto search = pos_map.find(complement); search != pos_map.end() && search->second != j) {
                return {j, search->second};
            }
        }
        return {0,0};
    }
};
