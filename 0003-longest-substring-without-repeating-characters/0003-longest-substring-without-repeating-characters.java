class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        HashMap <Character , Integer> last_seen = new HashMap<>(); 

        int l = 0 ; 
  
        int max_len = 0; 

        for(int r= 0; r < s.length(); r++){
            Character chr = s.charAt(r); 

            if (last_seen.containsKey(chr) && last_seen.get(chr) >= l){
                
                l = last_seen.get(chr) + 1;

            }
            last_seen.put(chr, r);
            max_len = Math.max(max_len , (r - l + 1)); 

        }

        return max_len ;

    }
}