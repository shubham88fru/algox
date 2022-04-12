##############################################
#SOL 1: Recursive way
#Average: T:O(log(N)), S:O(log(N)) 
#Worst: T:O(N), S:O(N)  <-- BST is a liner line. 
##############################################
# def findClosesValueInBst(tree, target):
#     return findClosestValueInBstHelper(tree, target, float("inf")) # "inf" --> infinity. Assuming here that inifinity is the closest value.

# def findClosestValueInBstHelper(tree, target, closest):       
#     #Base case
#     if tree is None:
#         return closest
#     if abs(target - closest) > abs(target - tree.value):
#         closest = tree.value
#     if target < tree.value:
#         return findClosestValueInBstHelper(tree.left, target, closest)
#     elif target > tree.value:
#         return findClosestValueInBstHelper(tree.right, target, closest)
#     else:
#         #means equal
#         return closest

###############################################
#SOL 2: Iteratively
#Average: T:O(log(N)), S:O(1)
#Worst: T:O(N), S:O(1)
###############################################
def findClosesValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf")) # "inf" --> infinity. Assuming here that inifinity is the closest value.

def findClosestValueInBstHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest