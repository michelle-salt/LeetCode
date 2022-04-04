/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int sum = 0;
    public int rangeSumBST(TreeNode root, int low, int high) {
        //traverse tree
        //if value in range, add to sum
        traversal(root, low, high);
        return sum;
    }
    
    private void traversal(TreeNode root, int l, int h) {
        if (root.val >= l && root.val <= h) {
            sum += root.val;
        }
        //traverse
        if (root.left != null) {
            traversal(root.left, l, h);
        }
        if (root.right != null) {
            traversal(root.right, l, h);
        } 
    }
}
