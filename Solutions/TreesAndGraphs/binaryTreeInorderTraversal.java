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
    List<Integer> list = new ArrayList<Integer>();
    public List<Integer> inorderTraversal(TreeNode root) {
        if (root == null) 
            return list;
        inorderHelper(root);
        return list;
    }
    
    public void inorderHelper(TreeNode root) {
        if (root.left == null) {
            list.add(root.val);
            if (root.right != null)
                inorderHelper(root.right);
        } else if (root.left != null) {
            inorderHelper(root.left);
            list.add(root.val);
            if (root.right != null) {
                inorderHelper(root.right);
            }
        }
    }
}
