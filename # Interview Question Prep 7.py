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



if __name__ == "__main__":
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    solution = Solution()
    nums = [2,0,2,1,1,0]
    #answer = solution.gameOfLife(board)
    answer = solution.sortColors(nums)




    