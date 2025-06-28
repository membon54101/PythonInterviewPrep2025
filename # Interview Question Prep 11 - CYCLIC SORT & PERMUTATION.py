class Solution:

    def findNumber(self, arr):
        arr.sort()
        answer = -1
        positive_list = list(filter(lambda x: x > 0, arr))

        #for idx, val in enumerate(arr):
        #    if val > 0:
        #        arr_test = arr[idx:]
        #        break
        #print(list(enumerate(arr)))

        for idx, val in enumerate(positive_list):
            if val != idx + 1:
                answer =  idx + 1
                break
        if answer < 0:
            answer = max(positive_list) + 1
        if answer == 0:
            answer + 1

        return answer
    
    def findNumbers(self, arr):
        arr.sort()
        
        for idx, num in enumerate(arr):
            if num != idx + 1:
                duplicate_num  = num
                arr = arr[:idx] + arr[idx+1:]
                break

        for idx, num in enumerate(arr):
            if num != idx + 1:
                missing_num = arr[idx] - 1

        return    [duplicate_num, missing_num]       

    def findPermutations(self, arr):
        if len(arr) == 0:
            return []
        if len(arr) == 1:
            return[arr]
        
        res = []

        for idx, val in enumerate(arr):
            rem = arr[:idx] + arr[idx+1:]
            for p in self.findPermutations(rem):
                res.append([val] + p)
        
        return res

    def findLongestChain(self, arr):
        arr.sort(key = lambda x: x[0])
        
        max_chain = 1 
        for idx, val in enumerate(arr):
            chain = [val]
            arr_dynamic = arr[idx + 1:]
            for idx2, val2 in enumerate(arr_dynamic):
                if arr_dynamic[idx2][0] > chain[-1][1]:
                    chain.append(val2)
                    print(chain, len(chain))
                else:
                    continue
            if len(chain) > 1 and len(chain) > max_chain:
                max_chain = len(chain)
        return max_chain
    
    def findLongestChain2(self, pairs):
        # Sort pairs based on their second element in ascending order
        pairs.sort(key=lambda x: x[1])
        
        currentEnd = float('-inf')  # Current end of the chain
        chainCount = 0  # Count of pairs in the chain
        print(pairs)
        # Iterate through the sorted pairs
        for pair in pairs:
            print(pair, currentEnd)
            # Check if the first element of the pair is greater than the current end
            if pair[0] > currentEnd:
                # Update the current end and increment the chain count
                currentEnd = pair[1]
                print(currentEnd)
                chainCount += 1

        return chainCount  # Return the maximum chain length
    
    def minAddToMakeValid(slef, str_inp):
        while '()' in str_inp:
            str_inp = str_inp.replace('()', '')

        #print(str_inp)
        return len(str_inp) 


if __name__ == '__main__':
    # https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/problem-challenge-2-find-the-smallest-missing-positive-number-medium
    solution = Solution()
    arr = [[7,8], [5,6], [1,2], [3,5], [4,5], [2,3]]
    str_input = "(()())("
    #answer = solution.findNumber(arr)
    # https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/solution-problem-challenge-1-find-the-corrupt-pair
    #answer = solution.findNumbers(arr)
    # https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/permutations-medium
    #answer = solution.findPermutations(arr)
    # https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/maximum-length-of-pair-chain-medium
    #answer = solution.findLongestChain(arr)
    #answer = solution.findLongestChain2(arr)
    # https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/minimum-add-to-make-parentheses-valid-medium
    answer = solution.minAddToMakeValid(str_input)
    print(answer)









