# https://www.geeksforgeeks.org/print-nodes-distance-k-given-node-binary-tree/
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/?envType=problem-list-v2&envId=7p5x763


class Solution:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

        # Function which finds the nodes at a given distance from root node


    def findNodes(root, dis, ans):

        # base case
        if root is None:
            return
        
        if dis == 0:
            ans.append(root.data)
            return
        
        # Here we recursively call the function 
        findNodes(root.left, dis - 1, ans)
        findNodes(root.right, dis - 1, ans)

    # Function which returns the distance of a node target node. Returns -1 if target is not found.
    def kDistanceRecur(root, target, k, ans):
        # base case
        if root is None:
            return -1
        
        # If current node is target
        if root.data == target:

            
             


if __name__ == "__main__":
    print('running directly')   










