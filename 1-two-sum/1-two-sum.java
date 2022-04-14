class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashSet<Integer> h = new HashSet<Integer>();
        for(int n: nums){
            h.add(n);
        }
        for(int i = 0; i < nums.length; i++){
            int comp = target - nums[i];
            if(h.contains(comp)){
                for(int j = i; j<nums.length; j++){
                    if(nums[j]==comp && i != j){
                        int[] ans = {i, j};
                        return ans;
                    }
                }
            }
        }
        int[] ans = {0,0};
        return ans;
    }
}