class Solution {
    public void rotate(int[] nums, int k) {
        //If k > nums.length, get k % nums.length
        //(new k) --> If k == 0 or k == nums.length, return unmodified nums
        
        //Get new first element (length -1) - k
        //create new array (new)
        //loop through all elements from firstNew to length -1 
            //Add each element to new array
        //loop through orig array from first to new first -1
            //Add each element to end of new array
        
        //return new array
        
        int length = nums.length;
        int newFirstIndex;
        int[] result = new int[length];
        
        if (k > length) {
            k %= length;
        }
        if (k!=0 && k!=length) {
                    
            newFirstIndex = length - k;
            for (int i = newFirstIndex; i < length; i++) {
                result[i-newFirstIndex] = nums[i];
            }   
            for (int i = 0; i < newFirstIndex; i++) {
                result[k+i] = nums[i];
            }
            
            for (int i = 0; i < length; i++) {
                nums[i] = result[i];
            }
        
        }
    }
}
