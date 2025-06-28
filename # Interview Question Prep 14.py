class Solution:
    def __init__(self):
        self.name = 'name' 

    # https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/factor-combinations-medium    
    def getAllFactors(self, n, result, curr, start):
        #print('n', n, 'result', result, 'curr', curr, 'start', start)
        for i in range(start, int(n**0.5) + 1):
                # running list of factors                
                if n % i == 0:
                    curr.append(i)
                    print('curr', curr, '[n // i]', [n // i]) 
                    result.append(curr + [n // i]) 
                    self.getAllFactors(n // i, result, curr, i)   
                    curr.pop()          
        return result
    
    def getFactors(self, n):
        return self.getAllFactors(n, [], [], 2)
    

    # https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/split-a-string-into-the-max-number-of-unique-substrings-medium
    def split_and_count(self, inp, start):
         unique_set = set()
         count = 0 
         for i in range(start, len(inp)):
              string = inp[start:i]
              if string not in unique_set:
                   unique_set.add(string)
              print(string)
         return count


    def maxUniqueSplit(self, inp):
         return self.split_and_count(inp, 0)
              

    

if __name__ == '__main__':
    sol = Solution()
    #res = sol.getFactors(20)
    res = sol.maxUniqueSplit("aab")
    print(res)





