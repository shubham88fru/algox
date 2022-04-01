#################################################
#Sol 1: two for loops
#T:O(N^2), S:O(1)

# def twoNumberSum(array, targetSum):
#     for i in range(len(array) - 1):
#         firstNum = array[i]
#         for j in range(i+1, len(array)):
#             secondNum = array[j]
#             if firstNum + secondNum == targetSum:
#                 return [firstNum, secondNum]
#     return []
##################################################

##################################################
#Sol 2: hashmap
#T: O(N), S: O(N)

# def twoNumberSum(array, targetSum):
#     nums = {}
#     for num in array:
#         potentialMatch = targetSum - num
#         if potentialMatch in nums:
#             return [potentialMatch, num]
#         else:
#             nums[num] = True
#     return []
##################################################

##################################################
#Sol 3: using start and pointer, and sort
#T: O(Nlog(N)), S: O(1)

def towNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right += 1
    return []
##################################################