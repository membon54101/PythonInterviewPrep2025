# Interview Question Prep
# https://www.hackerrank.com/interview/preparation-kits/three-month-preparation-kit/three-month-week-one/challenges

def plusMinus(arr):
    pos, neg, zer = 0, 0, 0
    for i in arr:
        if i < 0:
            neg += 1 
        elif i > 0:
            pos += 1
        else:
            zer += 1
            
    neg_ratio = neg /len(arr)     
    pos_ratio = pos /len(arr)
    zer_ratio = zer /len(arr)

    print( "{:.6f}".format(pos_ratio), '\n',  "{:.6f}".format(neg_ratio), '\n', "{:.6f}".format(zer_ratio))
#arr = [-4, 3, -9, 0, 4, 1]
#plusMinus(arr)

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    #print(arr[1:])
    min_num = sum(arr[:4])
    max_num = sum(arr[1:])
    print(min_num, max_num)
#arr = [1,3,5,7,9]
#miniMaxSum(arr)

def timeConversion(s):
    hour = int(s[:2])
    minute = int(s[3:5])
    second = int(s[6:8])
    if 'PM' in s and hour != 12:
        hour += 12
    if 'AM' in s and hour == 12:
        hour = 0

    time_simple = str('{:02}'.format(hour)) + ':' + str('{:02}'.format(minute)) + ":" + str('{:02}'.format(second))
    print(time_simple)
#s = '07:05:45PM'
#timeConversion(s)    

def breakingRecords(scores):
    min_counts, min_score, max_counts, max_score = 0, 0, 0, 0
    for i in range(len(scores)):
        if i == 0:
            min_score, max_score = scores[i], scores[i]  
        else:
            if scores[i] > max_score:
                max_counts = max_counts + 1
                max_score = scores[i]  
            if scores[i] < min_score:
                min_counts = min_counts + 1
                min_score = scores[i]  
        #print(min_counts, min_score, max_counts, max_score)

    return max_counts, min_counts
#scores = [12,24,10,24]
#breakingRecords(scores)

def camelCase(inp):
    output_camelCase = []
    for word in inp:
        finalWord = ''
        # If the operation is a split operation 
        if word[0] == 'S':
            for index, letter in enumerate(word[4:].replace('(', '').replace(')', '')):
                if letter.islower() == True:
                    finalWord = finalWord + letter
                else:
                    finalWord = finalWord + ' '+ letter.lower()         
        # If it is a concatenate
        if word[0] == 'C':
            word_strip = word[4:]
            # Method
            for index, letter in enumerate(word_strip):
                if letter != ' ' and word_strip[index - 1] != ' ':
                    finalWord = finalWord + letter
                elif word_strip[index - 1] == ' ':
                    finalWord = finalWord + letter.upper()
            if word[2] == 'M':
                finalWord = finalWord + '()' 
            if word[2] == 'C':
                finalWord = finalWord[0].upper() + finalWord[1:]

        output_camelCase.append(finalWord)
    print(output_camelCase)

#inp = ['S;M;plasticCup()', 'C;V;mobile phone', 'C;C;coffee machine', 'S;C;LargeSoftwareBook', 'C;M;white sheet of paper', 'S;V;pictureFrame']
#inp = ['S;V;iPad', 'C;M;mouse pad', 'C;C;code swarm', 'S;C;OrangeHighlighter']
#camelCase(inp)

#COULD NOT MAKE THIS WORK
def climbingLeaderboard(board, scores):
    ranking_array = []
    for score in scores:
        rank = 0
        for index, value in enumerate(board[:-1]):
            #print(index, value, board[index + 1], rank)
            if value != board[index + 1] and score > value:
                rank += 1
                ranking_array.append(rank)
                print(score, value, '###', rank)
            elif value != board[index + 1] and score < value:
                rank += 1
                print(score, value, 'LLLLL', rank)
            elif value == board[index + 1] and score > value and index != 0:
                ranking_array.append(rank)
                print(score, value, 'PPPP', rank)
            else:
                rank += 1
                print(score, value, 'YYY', rank)
        print(score, rank)
    return ranking_array




board = [100, 100, 50, 40, 40, 20, 10]
scores = [5, 25] #, 50, 120]

#ranking_array = climbingLeaderboard(board, scores)
#print(ranking_array)








