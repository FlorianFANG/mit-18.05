import numpy as np 
from itertools import groupby

nflips = 50
proba = 0.5
ntrials = 10000

samples = np.random.binomial(1, proba, size=(ntrials,nflips))
print(samples.shape)

def longest_seq(array):
    return max(sum(1 for i in g) for k,g in groupby(array))

res = np.apply_along_axis(longest_seq, axis=1, arr=samples)

print(f'average length of longest sequence = {np.mean(res)}')