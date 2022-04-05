#########################################
#Sol 1: while loop
#T: O(N), S(1)
#########################################
# def validateSubSequence(array, sequence):
#     arrIdx = 0
#     seqIdx = 0
#     while (arrIdx < len(array) and seqIdx < len(sequence)):
#         if array[arrIdx] == sequence[seqIdx]:
#             seqIdx += 1
#         arrIdx += 1
#     return seqIdx == len(sequence)
########################################

#######################################
#Sol 2: for loop
#T: O(N), S(1)
#######################################
def validateSubSequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            return True
        if value == sequence[seqIdx]:
            seqIdx += 1
    return seqIdx == len(sequence)
#######################################