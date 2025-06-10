class Solution:
    def platesBetweenCandles(self, s, queries):
        plates_in_between = []
        for i in queries:
            subs = s[i[0]: i[1]+1]
            #print(subs, '111111')
            if '|' in subs and '*' in subs:
                for idx, val in enumerate(subs):
                    if val == '|':
                        subs = subs[idx+1:]
                        #print(subs, '222')
                        break
                for idx, val in enumerate(subs[::-1]):
                        if val == '|' and subs[len(subs) - (idx + 2)] != '|':
                            subs = subs[:len(subs) - (idx + 1)]
                            #print(subs, '3333')
                            break
                        elif '|' not in subs:
                            subs = ''
                number_of_candles = len([i for i in subs if i == '|'])
                number_of_plates = len(subs) - number_of_candles
                plates_in_between.append(number_of_plates)
            else:
                plates_in_between.append(0)          
            return(plates_in_between)
        
    def canFinish(self, numCourses, prerequisites): 
        
        dic = {i: [] for i in range(len(prerequisites))}     

        # Map of course and prerequisites 
        for crs, pre in prerequisites:
            dic[crs].append(pre)
        print(dic)

        # Visit Sets - store all course on DFS path
        visits = set()

        # Depth First Functions
        def dfs(crs):
            # Base Case - Detected a loop - then we fail it 
            if crs in visits:
                 return False
            # Base Case 2 - there is no prerequisites for this course - then it can definitely be completed
            if dic[crs] == []:
                 return True
            #  Add the course to the visit - we will run the DFS on it 
            visits.add(crs)
            for pre in dic[crs]:
                if not dfs(pre): return False # We can return false if one course cannot be completed and the whole thing is false
            visits.remove(crs) # we no longer have to visit it
            dic[crs] = [] # so that we don't have to repeat the work of running dfs on neighbors if we have already gone through this once
            return True
            

        # Calling the DFS function
        for crs in range(numCourses):
                    if not dfs(crs): # if dfs(crs) == False then return false
                        return False
        return True
    
    def platesBetweenCandles_prefix_sum_array(self, s, queries): 
        # Generation of the prefix sum list   
        prefix_sum = [0] * (len(s))
        counter = 0 
        for idx, char in enumerate(s):
            if char == '*':
                counter += 1
            prefix_sum[idx] = counter
        #print('prefix_sum', prefix_sum)


        # Find nearest left/starting candle
        left_candle = [0] * (len(s))
        starting = -1
        for idx, char in enumerate(s):
                if char =='|':
                    starting = idx
                left_candle[idx] = starting
        #print('left_candle', left_candle)

        # Find nearest ending candle
        right_candle = [0] * (len(s))
        ending = -1
        for i in range(len(s) -1, -1, -1):
            if s[i] == '|':
                ending = i
            right_candle[i] = ending
        #print('right_candle', right_candle)

        result = [0] * len(queries)
        for idx, val in enumerate(queries):
            sub_right_candle = right_candle[val[0]]
            sub_left_candle = left_candle[val[1]]
            #print(sub_right_candle, sub_left_candle)

            if sub_left_candle != -1 and sub_right_candle != -1 and sub_right_candle < sub_left_candle:
                result[idx] = prefix_sum[sub_left_candle + 1] - prefix_sum[sub_right_candle + 1]
        print(result)
        return result         

    def platesBetweenCandles_prefix_sum_array_practice(self, s, queries): 
        # Generation of the prefix sum list   
        prefix_sum = [0] * len(s)
        px_sum = 0
        for idx, char in enumerate(s):
            if char == '*':
                  px_sum += 1
            prefix_sum[idx] = px_sum

        # Generate nearest candle to the right of plate
        right_ar = [0] * len(s)
        right_ct = -1
        for idx, char in enumerate(s):
            if char == '|':
                right_ct = idx
            right_ar[idx] = right_ct


        print('prefix_sum', prefix_sum)
        print('right_ar', right_ar)

        # Generate nearest candle to the left of plate
        left_ar = [0] * len(s)
        left_ct = -1
        for idx, char in reversed(list(enumerate(s))):
            if char == '|':
                  left_ct = idx
            left_ar[idx] = left_ct

        print('left_ar', left_ar)

        # Now loop through all queries
        result = [0] * len(queries)
        for idx, val in enumerate(queries):
            leftmost_candle = left_ar[val[0]] 
            rightmost_candle = right_ar[val[1]] 
            #print(leftmost_candle, rightmost_candle)
            if leftmost_candle != -1 and rightmost_candle != -1 and rightmost_candle > leftmost_candle:
                 result[idx] = (prefix_sum[rightmost_candle + 1] - prefix_sum[leftmost_candle + 1])
        #print(prefix_sum[rightmost_candle + 1], prefix_sum[leftmost_candle + 1])    
        
        print('result', result)
        return    
    
if __name__ == "__main__":


    # https://leetcode.com/problems/plates-between-candles/description/?envType=problem-list-v2&envId=7p5x763
    # Best Answer:  https://www.youtube.com/watch?v=4Ch3Zt5qGeA, 
    # https://www.youtube.com/watch?v=-1IsQyTM6Lg
    s = "***|**|*****|**||**|*"
    queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
    solution = Solution()
    #res = solution.platesBetweenCandles(s, queries)


    # DEPTH FIRST SEARCH
    # https://leetcode.com/problems/course-schedule/description/?envType=problem-list-v2&envId=7p5x763
    # https://medium.com/@yourstudybuddy/207-course-schedule-solution-and-explanation-in-details-7d6e982254f8
    # https://www.youtube.com/watch?v=EgI5nU9etnU
    numCourses = 2 
    prerequisites = [[0,1], [0,2], [1,3], [1,4], [3,4]]
    #res = solution.canFinish(numCourses, prerequisites)
    #print(res)

    #res = solution.platesBetweenCandles_prefix_sum_array(s, queries)
    res = solution.platesBetweenCandles_prefix_sum_array_practice(s, queries)










