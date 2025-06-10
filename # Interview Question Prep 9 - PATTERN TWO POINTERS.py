class Solution:

    def search(self, arr, target):
        answer = []
        lo, hi = 0, len(arr) - 1
        for i in range(len(arr)):
            while lo < hi:
                if arr[lo] + arr[hi] < target:
                     lo += 1
                elif arr[lo] + arr[hi] > target:
                     hi -= 1
                if arr[lo] + arr[hi] == target:
                    answer.append([arr[lo], arr[hi]])
                    while lo < hi and lo < len(arr) -1:
                        lo += 1

                print('n')


        print(answer)
        return answer   

    def moveElements(self, arr, target):
        result = list(sorted(set(arr)))
        print(result)
        return  result   
    
    def searchTriplets(self, arr, target):
        arr.sort()
        answers = []

        for idx, val in enumerate(arr):
            lo, hi = idx  + 1, len(arr) - 1
            while lo < hi: 
                total = val + arr[lo] + arr[hi]
                if  total > target or total == target:
                    hi -= 1    
                elif total < target:
                    for k in range(hi, lo, -1):
                        answers.append([arr[idx], arr[lo], arr[k]])
                    lo += 1    
                     
        print(answers)
        return  answers   


if __name__ == '__main__':
    import math
    # Design Gurus
    # https://www.designgurus.io/course-play/grokking-data-structures-for-coding-interviews/doc/problem-1-running-sum-of-1d-array-easy
    solution = Solution()
    arr = [-1, 4, 2, 1, 3]
    target = 5
    #answer = solution.search(arr, target)
    #answer = solution.moveElements(arr, target)
    answer = solution.searchTriplets(arr, target)





