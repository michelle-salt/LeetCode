class Solution {
    public int maxProfit(int[] prices) {
        int hold = -1;
        int profit = 0;
        for (int i = 0; i < prices.length; i++) {
            if (hold != -1) { //If you're holding
                if (i == prices.length -1) {
                    profit += prices[i] - prices[hold];
                } else if (prices[i+1] < prices[i]) {
                    profit += prices[i] - prices[hold];
                    hold = -1;
                }
            } else { //if not holding
                if (i != prices.length -1 && prices[i+1] > prices[i]) {
                    hold = i;
                }
            }
        }
        return profit;
    }
}
