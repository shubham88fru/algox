##############################################################################
# given special array - arrays inside array
# [5,2, [7, -1], 3, [6, [-13, 8], 4]]
# product sum is sum of each element multiplied by the depth of array
# Sol - T: O(N) where N is not simply the no. of elements in the outer most
# array, rather the total no. of elements including the elments in sub arrays
# S: O(D) where D is the depth of sub/special arrays
##############################################################################
def productSum(array, multiplier = 1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier+1)
        else:
            sum += element
    return sum * multiplier