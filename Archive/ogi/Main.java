import java.util.Stack;

public class Main {
    public static void main(String[] args) {

        String formulaInPostfix = "12+3+578/-*";
        Node root = Node.buildTree(formulaInPostfix);
        Node.printTree(root);

    }
}


class Node {
    char c;
    int level, count;
    Node left, right;

    public Node(char c) {
        this.c = c;
        this.left = this.right = null;
    }
    
    
    public static Node buildTree(String formulaInPostfix) {
        Stack<Node> stack = new Stack<>();

        int len = formulaInPostfix.length();    // Length of the formula.
        int height = findHeight(len);           // Height of the tree.

        for (int i = 0; i < len; i++) {
            char c = formulaInPostfix.charAt(i);

            if (c >= 48 && c <= 57) {   // If c is a number, push it to the stack.
                Node node = new Node(c);
                node.level = height;  // Leaf nodes are at level 1
                stack.push(node);
            } if (c == 42 || c == 43 || c == 45 || c == 47) { // If c is an operator, pop two elements from the stack and create a new node with c as the root.
                Node right = stack.pop();
                Node left = stack.pop();

                Node node = new Node(c);
                node.left = left;
                node.right = right;
                node.level = Math.min(left.level, right.level) - 1;  // The level of a node is one less than the minimum level of its children.

                stack.push(node);
            }
            
        }
        Node root = stack.pop();    // The last element in the stack is the root of the tree.
        return root;                // Return the root.
    }

    public static int getHeight(Node root) {    // Function to find the height of the tree.
        if (root == null) {
            return 0;
        }
        int leftHeight = getHeight(root.left);
        int rightHeight = getHeight(root.right);

        return Math.max(leftHeight, rightHeight) + 1;
    }

    public static int findHeight(int len) {    
        int height = 0;
        while (Math.pow(2, height) < len) {
            height++;            
        }
        return height;
    }


    static void printInfix(Node node, Stack<Node> stack) {
        if (node == null) {
            return;
        }
        printInfix(node.left, stack);
        stack.push(node);
        printInfix(node.right, stack);
    }

    public static void printTree(Node root) {
        int height = getHeight(root);                   // Height of the tree.
        int width = (int) Math.pow(2, height+1) - 1;  // Width of the tree.
        char[][] grid = new char[height][width];        // 2D array to store the tree.

        for (int i = 0; i < height; i++) {              // Fill the grid with spaces.
            for (int j = 0; j < width; j++) {
                grid[i][j] = ' ';
            }
        }

        Stack<Node> stack = new Stack<>();          // Stack to store the nodes in infix order.
        Node.printInfix(root, stack);           
        int column = 0;                             // Integer to keep track of the column of the node.
        for (Node node : stack) {               
            node.count = column++;                  // Count is the column of the node.
            grid[node.level-1][node.count] = node.c;// Fill the grid with the nodes.
        }
        
        for (int i = 0; i < height; i++) {              // Print the grid.
            for (int j = 0; j < width; j++) {
                System.out.print(grid[i][j]);
            }
            System.out.println();
        }
    }
    
}