# input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
# output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21

ht = {}

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    for num in weights:
        if num not in ht:
            ht[num] = weights.index(num)
    return None


weights = [ 4, 6, 10, 15, 16 ]
length = 5
limit = 21
get_indices_of_item_weights(weights,length,limit)
print("ht: ", ht)
# keys = ht.keys()
# sum = 0
# for num in keys:
#     sum += num
# print("sum: ", sum)