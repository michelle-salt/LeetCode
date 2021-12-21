class Solution {
    public int reverse(int x) {
        String strX = String.valueOf(x);
        String result = "";
        if (strX.substring(0,1).equals("-")) {
            result = "-";
            strX = strX.substring(1);
        } 
        while (strX.length() > 1) {
            result += strX.substring(strX.length()-1);
            strX = strX.substring(0, strX.length()-1); 
        }
        result += strX;
        if (Long.parseLong(result) >= Math.pow(2, 31)-1 || Long.parseLong(result) <= -1*Math.pow(2, 31)) {
            return 0;
        }
        
        return Integer.parseInt(result);
    }
}
