import numpy as np 

ntrials = 10000

def sim_PB():
    print(f'P(B) simulation')
    for n in range(1,100):
        samples = np.random.randint(1,366,size=(ntrials, n))
        count = 0
        for trial in range(1, ntrials):
            u = np.unique(samples[trial])
            if u.shape[0] < n:
                count += 1
        print(f'n = {n}: P(B) = {round(count/ntrials,5)}', flush=True)

if __name__ == '__main__':
    sim_PB()