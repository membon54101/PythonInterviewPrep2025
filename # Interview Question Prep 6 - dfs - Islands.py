class Solution:

    def dfs(self, grid, r, c, visited):

        rNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        cNbr = [-1, 0, 1, -1, 1, -1, 0, 1]

        # Mark this cell as visited
        visited[r][c] = True

        # Recur for all connected neighbours
        for k in range(8):
            newR, newC = r + rNbr[k], c + cNbr[k]

            # Is is safe 
            row = len(grid)
            col = len(grid[0])
            if (0 <= newR < row) and (0 <= newC < col) and (grid[newR][newC] == 'L' and not visited[newR][newC]):
                self.dfs(grid, newR, newC, visited)

    def countIslands(self, grid):
        if not grid:
            return 0 
        
        row, col = len(grid), len(grid[0])
        
        # Either one of these 
        visited = [[False for _ in range(col)] for _ in range(row)]
        visit = set()

        count = 0
        for r in range(row):
            for c in range(col):
                
                # If a cell with value 'L' (land) is not visited yet,
                # then a new island is found
                if grid[r][c] == 'L' and not visited[r][c]:
                    
                    # Visit all cells in this island.
                    self.dfs(grid, r, c, visited)
                    
                    # increment the island count
                    count += 1
        print(count)
        return count

    
if __name__ == "__main__":

    solution = Solution()
    grid = [
        ['L', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'L'],
        ['L', 'W', 'W', 'L', 'L'],
        ['W', 'W', 'W', 'W', 'W'],
        ['L', 'W', 'L', 'L', 'W']
    ]

    # https://www.youtube.com/watch?v=gCswsDauXPc
    res = solution.countIslands(grid)

    # https://leetcode.com/problems/path-sum-ii/description/?envType=problem-list-v2&envId=954v5ops










