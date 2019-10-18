import numpy as np 

ntrials = 10000

def birthday_match(match_num: int):
    print(f'\nSimulation for {match_num} match:', flush=True)
    for n in range(1,100):
        samples = np.random.randint(1,366,size=(ntrials, n))
        count = 0
        for trial in range(1, ntrials):
            u,c = np.unique(samples[trial], return_counts=True)
            if match_num in c:
                count += 1
        print(f'n = {n}: P(B) = {round(count/ntrials,5)}', flush=True)

if __name__ == '__main__':
    birthday_match(2)
    birthday_match(3)