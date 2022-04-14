class Solution {
    public int lengthOfLongestSubstring(String s) {
        int start=0, end =0;
        int len = end-start;
        HashSet<Character> h = new HashSet<Character>();
        while(end<s.length()){
            if(!h.contains(s.charAt(end))) h.add(s.charAt(end++));
            else h.remove(s.charAt(start++));
            len = Math.max(len, h.size());
        }
        return len;
    }
}