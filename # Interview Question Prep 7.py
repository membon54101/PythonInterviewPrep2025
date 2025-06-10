class Solution:
    def gameOfLife(self, board):
        rows = len(board)
        cols = len(board[0])

        rowShift = [-1, -1, -1, 0, 0, 1, 1, 1]
        colShift = [1, 0, -1, 1, -1, 0, -1, 1]

        new_board = [[1 for i in range(cols)] for ii in range(rows)]
        for idx, val in enumerate(board):
            for idx2, val2 in enumerate(val):
                live_count = 0
                dead_count = 0
                for k in range(len(rowShift)):
                    if idx + rowShift[k] >= 0 and idx2 + colShift[k] >= 0 and idx + rowShift[k] < (len(board) - 1) and idx2 + colShift[k] < (len(board)- 1):
                        testing_cell = board[idx + rowShift[k]][idx2 + colShift[k]]
                        if testing_cell == 0:
                            dead_count += 1
                        if testing_cell == 1:
                            live_count  += 1
                    
                    # Start Populating the new board  
                    print('idx', idx, 'idx2', idx2, 'live_count', live_count, 'dead_count', dead_count)          
                if board[idx][idx2] == 1 and live_count < 2:
                    new_board[idx][idx2] = 0
                elif board[idx][idx2] == 1 and (live_count == 2 or live_count == 3):
                    new_board[idx][idx2] = 1
                elif board[idx][idx2] == 1 and live_count > 3:
                    new_board[idx][idx2] = 0
                elif board[idx][idx2] == 0 and  live_count == 3:
                    new_board[idx][idx2] = 1
                else: new_board[idx][idx2] = board[idx][idx2]

        print(new_board)
        return new_board       
                    
    def sortColors(self, nums):
        print(sorted(nums))

    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
    
        # Create a DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        print(dp)
        
        # Initialize first row and column
        for i in range(m + 1):
            dp[i][0] = i  # Converting word1[0..i] to empty string
        for j in range(n + 1):
            dp[0][j] = j  # Converting empty string to word2[0..j]
        print (dp)

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]  # Characters match, no operation needed
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],    # deletion
                        dp[i][j-1],    # insertion
                        dp[i-1][j-1]   # replacement
                )
        print(dp, dp[m][n])
        return dp[m][n]


    def queensAttack(self, n, k, q, obstacles):
        board = [[0 for _ in range(n)] for _ in range(n)] 

        # Base Cases
        if n <= 1 or k == 0:
            return 0 
    
        #Place Queen
        queen_row, queen_col = n  - q[0], q[1] - 1
        board[queen_row][queen_col] = 'Q'

        # Place Obstacles 
        for i in obstacles:
            board[n - i[0]][i[1] - 1] = 'O'

        directional_moves = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1,1]]
        
        moves = 0 
        for idx, val in enumerate(directional_moves):
            is_open = True
            multiplier = 1
            #print(val, 'here')
            while is_open == True and (queen_row + val[0] * multiplier) in range (0, n)  and (queen_col + val[1]* multiplier) in range(0, n) :
                #print('piece', board[queen_row + val[0] * multiplier][queen_col + val[1]* multiplier])
                if board[queen_row + val[0] * multiplier][queen_col + val[1]* multiplier] != 'O':
                    #print(val, multiplier, moves)
                    moves += 1
                    multiplier +=1 
                else: 
                    #print(val, 'False')
                    is_open = False
        print(moves)
        return
    
    def Fibonacci(self, t1, t2, n):
        arr = [0] * n 
        arr[0], arr[1] = t1, t2
        for i in range(2,n):
            arr[i] = arr[i - 2] + arr[i-1]**2

        print(arr) 
        return 

if __name__ == "__main__":
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    solution = Solution()
    nums = [2,0,2,1,1,0]
    #answer = solution.gameOfLife(board)
    #answer = solution.sortColors(nums)
    #https://leetcode.com/problems/edit-distance/
    word1 = "horse"
    word2 = "ros"
    #answer = solution.minDistance(word1, word2)

    #https://www.hackerrank.com/challenges/queens-attack-2/problem
    n = 5
    k = 3
    q = (4,3)
    obstacles = [(5,5), (4,2), (2,3)]
    answer = solution.queensAttack(n, k, q, obstacles)
    
    # https://www.hackerrank.com/challenges/fibonacci-modified/problem
    t1 = 0
    t2 = 1
    n = 6
    #answer = solution.Fibonacci(t1, t2, n) 
    #print(answer)



