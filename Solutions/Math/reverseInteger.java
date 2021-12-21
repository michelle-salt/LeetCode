class Solution {
    public int reverse(int x) {
        int numChars = 0;
        long l = 0;
        if (x < 0) {
            numChars = String.valueOf(x).length() - 1;
            
        } else {
            numChars = String.valueOf(x).length();
        }
        for (int i = 0; i < numChars; i++) {
            l += (x%10)*Math.pow(10,(numChars-i)-1);
            x /= 10;
        }
        
        if (l >= Math.pow(2, 31)-1 || l <= -1*Math.pow(2, 31)) {
            return 0;
        }
        return (int)l;
    }
}
