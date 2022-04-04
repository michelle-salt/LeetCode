/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    List<Integer> list = new ArrayList<Integer>();
    public List<Integer> preorder(Node root) {
        preorderHelper(root);
        return list;
    }
    
    public void preorderHelper(Node root) {
        if (root != null) {
            list.add(root.val);
            if (root.children == null) {
                //Do nothing
            } else {
                for (int i = 0; i < root.children.size(); i++) {
                    preorderHelper(root.children.get(i));
                }
            }
        }
    }
}
