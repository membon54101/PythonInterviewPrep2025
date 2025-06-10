class Solution:

    def stockmax(self, prices):
          
        running_max = 0
        profit = 0
        for price in reversed(prices): # Iterate backward over the prices
            running_max = max(running_max, price) # Update the running maximum price
            profit += running_max - price # Add potential profit for the current day
        print(profit)
        return profit

    def stockmax2(self, prices):
        # Write your code here
        print(list(enumerate(prices)))
        sorted_prices = sorted(list(enumerate(prices)), key=lambda x: x[1], reverse=True)
        tot_gained = 0
        price_pointer = 0
        for curr_idx in range(len(prices)):
            if curr_idx < sorted_prices[price_pointer][0]:
                tot_gained += sorted_prices[price_pointer][1] - prices[curr_idx]
            else:
                n = 1
                while price_pointer + n < len(prices) and sorted_prices[price_pointer+n][0] < sorted_prices[price_pointer][0]:
                    n += 1
                price_pointer += n
            curr_idx += 1
        
        return tot_gained
    
    def threeSum(self,q):
        # https://www.youtube.com/watch?v=wCe-MeqXgMc
        q.sort()
        n = len(q)
        answer = []
        for idx, num in enumerate(q):
            if num == q[idx - 1] and idx > 0:
                continue
            if num > 0:
                break
            # 2-sum on remainder of list 
            lo, hi = idx + 1, n - 1

            while lo < hi:
                total = num + q[lo] + q[hi]
                if total > 0:
                    hi -= 1
                elif total < 0:
                    lo += 1
                else:
                    answer.append([num, q[lo], q[hi]])
                    lo += 1
                    # To prevent double counting values
                    while lo < hi and q[lo] == q[lo - 1]:
                        lo += 1
        print(answer)
        return answer

if __name__ == '__main__':

    # https://www.hackerrank.com/challenges/three-month-preparation-kit-stockmax/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-nine
    prices = [1, 2, 100, 150, 80, 70]
    solution = Solution()
    #solution.stockmax(prices)

    # https://leetcode.com/problems/3sum/description/
    q = [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]
    solution.threeSum(q)








