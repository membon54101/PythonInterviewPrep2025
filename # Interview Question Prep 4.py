# https://leetcode.com/problems/house-robber/description/
class Solution:

    #def __init__ (self, name):
    #    self.name = name

    def rob(self, nums):
        robbings_odd = 0 
        robbings_even = 0 
        for i in range(0, len(nums), 2):
            robbings_odd += nums[i]
        for i in range(1, len(nums), 2):
            robbings_even += nums[i]

        #print (robbings_even, robbings_odd)
        return max(robbings_even, robbings_odd)
    

    def lilysHomework(self, arr):
        swaps = 0
        for idx, val in enumerate(arr):
            min_val = min(arr[idx:])
            if val != min_val:
                arr[arr.index(min_val)] = val
                arr[idx] = min_val
                swaps += 1
                print(arr)
        print(swaps)
        return swaps

    def reorderLogFiles(self, logs):
        final_log = []
        let_logs = []
        dig_logs = []
        for idx, val in enumerate(logs):
            if val.split(' ')[1].isalpha(): #r'[a-zA-Z]' in val.split(' ')[1]:
                let_logs.append(val)
            else:
                dig_logs.append(val)

        dict = {' '.join(val.split(' ')[1:]):  val.split(' ')[0] for idx, val in enumerate(let_logs)}
        #value_sorted = list(dict.values())
        value_sorted = list(dict.keys())

        for i in sorted(value_sorted):
            i = dict[i] + ' '  +  i 
            final_log.append(i)
           
        
        final_log = final_log + dig_logs

        print(final_log)
        return final_log
        
        




#if __name__ == "__main__":
nums = [2,7,9,3,1]
solution = Solution()
#result = solution.rob(nums)
#print(result)

# https://www.hackerrank.com/challenges/three-month-preparation-kit-lilys-homework/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-eleven

arr = [2,7,9,3,1,15,10,4,8]
#swaps = solution.lilysHomework(arr)

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
logs = ["a1 9 2 3 1","g1 bct car","zo4 4 7","ab1 off key dog","a8 act zoo", "g2 act car",]
arranged_log = solution.reorderLogFiles(logs)










