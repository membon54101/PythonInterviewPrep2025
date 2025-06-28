class Solution:
    def __init__(self):
        self.findMedianClass = findMedianClass()
        self.maxHeap = []
        self.minHeap = []

class findMedianClass:
    
    def insertNum(slef, num, running_list):
        running_list.append(num)
        return
    
    def findMedian(self, running_list):
        running_list.sort()
        print(running_list)
        if len(running_list) % 2 != 0:
            index_num = math.ceil(len(running_list)/2)
            return running_list[index_num - 1]
        else:
            index_ceil = int(len(running_list)/2)
            index_floor = int((len(running_list)/2) - 1)
            print(index_ceil, index_floor)
            return (running_list[index_floor] + running_list[index_ceil]) / 2
        
    def insertNum_heap(self, num):
        if not self.maxHeap or 



if __name__ == '__main__':
    import math
    from heapq import * 
    solution = Solution()
    findMedianClass_int1 = findMedianClass()
    running_list = []
    findMedianClass_int1.insertNum(3, running_list)
    findMedianClass_int1.insertNum(1, running_list)
    findMedianClass_int1.insertNum(5, running_list)
    findMedianClass_int1.insertNum(4, running_list)
    findMedianClass_int1.insertNum(7, running_list)
    findMedianClass_int1.insertNum(9, running_list)
    findMedianClass_int1.insertNum(12, running_list)
    findMedianClass_int1.insertNum(1, running_list)
    result = findMedianClass_int1.findMedian(running_list)
    print(result)




