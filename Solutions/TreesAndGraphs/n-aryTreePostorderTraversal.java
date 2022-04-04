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
    public List<Integer> postorder(Node root) {
        if (root == null)
            return list;
        postorderHelper(root);
        return list;
    }
    
    public void postorderHelper(Node root) {
        if (root.children == null) {
            list.add(root.val);
        } else {
            for (int i = 0; i < root.children.size(); i++) {
                postorderHelper(root.children.get(i));
            }
            list.add(root.val);
        }
    }
}
