# Jesse and Cookies
def cookies(k, A):
    # Write your code here
    #no_baking = True
    #for i in A:
    #    if i < k:
    #        no_baking = False
    #if no_baking == True:
    #    return 'No baking needed'
    
    A.sort()
    if min(A) >= k:
        return 'No baking needed'
    
    iters = 0
    while min(A) < k:
        new_val = A[0] + A[1] * 2
        #print([new_val], '********', A[2:])
        A = [new_val] + A[2:]
        iters +=1 
        A.sort()
        #print(A)
    return iters
    
k = 7
A = [10, 11, 9, 9, 14, 50]
A = [2, 3, 7, 6, 4, 6]
A = [1, 2, 3, 9, 10, 12]
#res = cookies(k, A)
#print(res)

def rotate_matrix_90_clockwise(matrix):
    for i in range(len(matrix)):
        for ii in range(i, len(matrix)):
            print(i, ii, matrix[i][ii], matrix[ii][i])
            matrix[i][ii], matrix[ii][i] =  matrix[ii][i], matrix[i][ii]
            #print(matrix[i][ii], matrix[ii][i])
    for r in matrix:
        r.reverse()

    print(matrix)
    return matrix

def rotate_matrix_90_clockwise2(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix with dimensions swapped
    rotated_matrix = [[0] * rows for _ in range(cols)]
    print(rotated_matrix)
    # Populate the new matrix with rotated values
    for i in range(rows):
        for j in range(cols):
            rotated_matrix[j][rows - 1 - i] = matrix[i][j]

    return rotated_matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#res = rotate_matrix_90_clockwise2(matrix)
#print(res)


# Highest Value Palindrome
# https://www.geeksforgeeks.org/make-largest-palindrome-changing-k-digits/
def highestValuePalindrome2(str1, k):
    s = list(str1)
    n = len(s)
    arr = []
    replacements = 0 

    # First make it a palindrome
    for idx, val in enumerate(s[:math.floor(len(s)/2)]):
        if val != s[len(s)-1-idx]:
            if replacements >= k:
                return 'Not enough swaps available to get to a palindrome'
            else:
                new_val = max(s[idx], s[len(s)-1-idx])
                s[idx], s[len(s)-1-idx] = str(new_val), str(new_val)
                replacements += 1

    # change the middle number 
    middle_digit = math.ceil(len(s)/2) - 1
    if s[middle_digit] != '9' and replacements < k and len(s) % 2 != 0:
        s[middle_digit] = '9'
        replacements += 1

    # Start changing the minimum value pairs 
    min_val  = min(s)
    for idx, value in enumerate(s):
        if value == min_val and (replacements <= k - 2):
            s[idx], s[len(s)-1-idx] = '9', '9'
            replacements += 2

    return s


import math
s = '092282'
k = 4
#s_changed = highestValuePalindrome2(s, k)
#print(s_changed)

def leastBricks(wall):
    # calculate width of call
    w = sum(wall[0])    
    
    arr_2d = []
    for i in range(len(wall)):
        arr = []
        for ii in range(len(wall[i])):
                sum_working = sum(wall[i][:ii])
                arr.append(sum_working)
        arr_2d.append(arr)
    #print(arr_2d)

    counter_old = 0
    for i in range(1,w):
        counter = 0
        for ii in arr_2d:
            if i in ii:
                counter += 1
        if counter > counter_old:
            counter_old = counter
        #print(i, counter, counter_old)

    return (w - counter_old)
      

wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
#wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,3],[1,3,1,1]]    
res = leastBricks(wall)
print(res)



