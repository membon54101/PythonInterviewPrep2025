class Solution:

    def find(self, target):
        results_arr = []
        result = 0
        while result != 1:
            result = 0
            for i in str(target):
                    result += int(i)**2
            if result == 1:
                 return True
            if result in results_arr:
                return False
            results_arr.append(result)
            target = result
            print(result)

        return True   
    

    def merge_intervals(self, intervals):
        if not intervals:
            return []

        # Sort intervals based on start times
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            print('interval', interval)
             # if the list of merged intervals is empty or if the current interval does not overlap with the last interval, append it
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Otherwise, there is an overlap, so merge the current interval with the last one
                print('merged', merged[-1][1])
                merged[-1][1] = max(merged[-1][1], interval[1])
                print('22222', merged, interval[1])
            print('interval22', interval, merged)
        return merged
    
    def insert(self, arr, new_interval):
        arr.append(new_interval)
        arr.sort(key = lambda x: x[0])
        merged = []

        if len(arr) <= 1:
            return arr

        for idx, val in enumerate(arr):
            if idx == 0 or merged[-1][1] < val[0]:
                merged.append(val)
            else: 
                merged[-1][1] = max(merged[-1][1] , val[1])
            print('merg', merged)
        return merged
    
    def intersection(self, arr, new_arr):
        arr.sort(key = lambda x: x[0])
        if len(arr) < 1: return []

        overlap = []
        for idx, val in enumerate(new_arr):
            for idx2, val2 in enumerate(arr):
                if (val[0]  <= val2[1] and val[0] >= val2[0]):
                    overlap.append([val[0], min(val[1], val2[1])])
                elif val[1] <= val2[1] and val[0] <= val2[0] and val[1] >= val2[0]:
                    overlap.append([max([val[0], val2[0]]), min([val[1], val2[1]])])
                    print('pppp', val, val2)
                elif val[1] == val2[0]:
                    overlap.append([val[1], val[1]])

        print(overlap)
        return


    def interval_intersection(self, firstList, secondList):
        result = []
        i, j = 0, 0

        while i < len(firstList) and j < len(secondList):
            start_max = max(firstList[i][0], secondList[j][0])
            end_min = min(firstList[i][1], secondList[j][1])

            if start_max <= end_min:
                result.append([start_max, end_min])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
            print(result)
        
        return result
    
    def canAttendAllAppointments(self, arr):
        result = True
        arr.sort(key = lambda x: x[0])
        for idx, val in enumerate(arr):
            if idx < len(arr) - 1 and val[1] > arr[idx+1][0]:
                result =  False
                break
        return result
    
    def intersection2(self, arr1, arr2):
        intersects = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            print(arr[i], arr2[j])
            start = max(arr[i][0], arr2[j][0])
            end = min(arr[i][1], arr2[j][1])

            if arr[i][1] >= arr2[j][0]:
                intersects.append([start, end])
            if arr[i][1] < arr2[j][1]:
                i += 1
            else:
                j += 1

        return intersects
                

if __name__ == '__main__':
    # https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/happy-number-medium
    solution = Solution()
    tester = 12
    #answer = solution.find(tester)
    # https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/merge-intervals-medium
    arr =  [[1, 3], [5, 7], [9, 12]]
    new_arr = [[5, 10]]
    #answer = solution.merge_intervals(arr)
    #answer = solution.insert(arr, new_arr)
    #answer = solution.interval_intersection(arr, new_arr)
    #answer = solution.canAttendAllAppointments(arr)
    answer = solution.intersection2(arr, new_arr)
    print(answer)








