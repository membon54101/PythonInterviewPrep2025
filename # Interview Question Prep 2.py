# Sort the 'ranked' array so we can get a structured leaderboard.
def climbingLeaderboard(ranked, player):
    leaderboard = sorted(set(ranked), reverse=True)
# Get the length of the leaderboard to track where we are at each iteration.
    l = len(leaderboard)
    print('leaderboard', leaderboard, l)
    new_ranked = []    # empty array for storing our ranked results

# Loop through the 'player' array and compare against our leaderboard logic.
# 'leaderboard[l - 1]' because leaderboard is a 0 index array
    for score in player:
        print('l', l)
        while (l > 0) and (score >= leaderboard[l - 1]):     
            print('score', score, 'l', l, 'leaderboard[l - 1]', leaderboard[l - 1])   
            l -= 1                # Go up the leaderboard 
        new_ranked.append(l+1)    # increase the rank by 1 if score is less than a current rank.

    return new_ranked

# Sort the 'ranked' array so we can get a structured leaderboard.
def climbingLeaderboard2(ranked, player):
    leaderboard = sorted(set(ranked), reverse=True)
# Get the length of the leaderboard to track where we are at each iteration.
    l = len(leaderboard)
    print(leaderboard)
    new_ranked = []    # empty array for storing our ranked results

# Loop through the 'player' array and compare against our leaderboard logic.
# 'leaderboard[l - 1]' because leaderboard is a 0 index array
    for score in player:
        r = 1
        while r <= l and score <= leaderboard[r - 1]:
            print('score_processed', score, 'r', r, 'leaderboard[r - 1]', leaderboard[r - 1], new_ranked)
            r += 1
        new_ranked.append(r)
        

    return new_ranked

#new_ranked = climbingLeaderboard2([100, 90, 90, 80, 70], [70, 80, 105, 95, 75])
#print(new_ranked)


def minimumBribes(q):
    swaps = 0
    out_of_order = True
    while out_of_order:
        out_of_order = False
        for idx, value in enumerate(q[:-1]):
            if value - (idx + 1) > 2:
                return 'too chaotic'
            if value == idx + 1:
                next
            if value > q[idx + 1]:
                q[idx+1], q[idx] = q[idx], q[idx+1]
                swaps += 1
                out_of_order = True
    return swaps
            
"""    for index, value in enumerate(q):
        if value - (index + 1) == 0: 
            print('value', value, 'index', index + 1)
            next 
        elif value - (index + 1) == 1:
            print(value, 'here')
            swaps = swaps + 1
        elif value - (index + 1) == 2:
            print(value, 'here2')
            swaps = swaps + 2
        elif value - (index + 1) > 2:
            return 'too chaotic'
    return swaps
"""
q = [1,2,5,3,7,8,6,4]

#q = [1, 3, 5, 2, 4, 8, 6, 7]
#res = minimumBribes(q)
#print(res)


# The Maximum Subarray
def maxSubarray(arr):
    max_subsequence = sum(i for i in arr if i > 0 )
    max_subarray = 0
    for i in range(len(arr)):
        for ii in range(i, len(arr) + 1):
            x = sum(arr[i:ii])
            if x > max_subarray:
                max_subarray = x             
    return max_subsequence, max_subarray


arr = [-1, 2, 3, -4, 5, 10]   
max_subsequence, max_subarray = maxSubarray(arr)
print(max_subsequence, max_subarray)



