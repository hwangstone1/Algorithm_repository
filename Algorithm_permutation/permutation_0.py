# import itertools
#
# arr = ['A', 'B', 'C']
# nPr = itertools.permutations(arr, 2)
# print(list(nPr))

import itertools, time

array = list(map(str, input().split()))
start = time.time()
nPr = itertools.permutations(array, 3)
end = time.time()
print(list(nPr), start - end)
