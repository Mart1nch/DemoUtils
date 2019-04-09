package tree;


public class BinaryTree {
    private TreeNode root;

    public BinaryTree() {
    }

    public BinaryTree(TreeNode root) {
        this.root = root;
    }

    public TreeNode getRoot() {
        return root;
    }

    public void setRoot(TreeNode root) {
        this.root = root;
    }


    /**
     * 返回父节点
     * 参数 根节点、目标节点
     * */
    public TreeNode getParent(TreeNode subTree, TreeNode element) {
        if (subTree == null)
            return null;

        if (subTree.getLeft() == element || subTree.getRight() == element)
            return subTree;

        TreeNode treeTemp = null;
        //递归查找
        if ((treeTemp = getParent(subTree.getLeft(), element)) != null)
            return treeTemp;
        else
            return getParent(subTree.getRight(), element);
    }

    /**
     * 返回二叉树节点个数
     * */
    public int getSize(TreeNode node){
        if (node == null){
            return 0;
        }else{
            int i = getSize(node.getLeft());
            int j = getSize(node.getRight());
            return (i + j + 1);
        }
    }

    /**
     * 返回树的高度
     * */
    public int getHeight(TreeNode node){
        if (node == null){
            return 0;
        }else {
            int i = getHeight(node.getLeft());
            int j = getHeight(node.getRight());
            return (i > j) ? (i + 1) : (j + 1);
        }
    }

    /**
     * 前序遍历
     * */
    public void preOrder(TreeNode node){
        if (node != null){
            System.out.println(node.getData());
            preOrder(node.getLeft());
            preOrder(node.getRight());
        }

    }

    /**
     * 中序遍历
     * */
    public void inOrder(TreeNode node){
        if (node != null){
            inOrder(node.getLeft());
            System.out.println(node.getData());
            inOrder(node.getRight());
        }

    }

    /**
     * 后序遍历
     * */
    public void postOrder(TreeNode node){
        if (node != null){
            postOrder(node.getLeft());
            postOrder(node.getRight());
            System.out.println(node.getData());
        }

    }

    /**
     * 默认后序遍历
     * */
    public void postOrder(){
        if (root != null){
            postOrder(root.getLeft());
            postOrder(root.getRight());
            System.out.println(root.getData());
        }

    }

    /**
     * 销毁二叉树
     * */
    public void deleteTree(TreeNode node){
        if (node != null){
            deleteTree(node.getLeft());
            deleteTree(node.getRight());
            node = null;
        }
    }

    /**
     *  默认销毁二叉树
     * */
    public void deleteTree(){
        if (root != null){
            deleteTree(root.getLeft());
            deleteTree(root.getRight());
            root = null;
        }
    }
}
