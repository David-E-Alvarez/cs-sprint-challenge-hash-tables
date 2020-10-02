list_of_lists = [
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1,]
]

#can i cache all the arrays?
cache = {}
intersection = []

for i in range(len(list_of_lists)):
    #print(list_of_lists[i])#prints each list in "list_of_lists" array
    for elem in list_of_lists[i]:
        print("---->",elem)
        if elem in cache:
            cache[elem] += 1
        else: 
            cache[elem] = 0
        print('----->', cache)
    print("------------")

