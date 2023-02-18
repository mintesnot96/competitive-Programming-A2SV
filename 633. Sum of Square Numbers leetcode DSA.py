class Solution {
    public boolean judgeSquareSum(int c) {
        HashSet<Long> nums = new HashSet<>();
        for (int i = 0; i <= Math.sqrt(c); i ++) {
            nums.add((long)i*i);
            if (nums.contains((long)(c - i*i))) {
                return true;
            }
        }
        return false;
    }
}
