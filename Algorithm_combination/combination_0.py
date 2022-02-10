import itertools, time
array = ['A', 'B', 'C']
start = time.time()
nCr = itertools.combinations(array, 2)
end = time.time()
ttime = start-end
print(list(nCr), ttime)