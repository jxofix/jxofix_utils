import statistics
import random
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def binom_test():
    alpha = 0.05
    pval = stats.binom_test(1, n=10, p=0.5, alternative='two-sided')

    print('pvalue = ', pval)


def gen_random_variable(num):
    nums = []
    for i in range(0, num):
        nums.append(random.randrange(10))

    return statistics.mean(nums)


def view_hist(num):
    data = []
    n_bins = 20
    for _ in range(0, num):
        data.append(gen_random_variable(10))

    fig, axs = plt.subplots(1)

    # We can set the number of bins with the *bins* keyword argument.
    axs.hist(data, bins=n_bins)
    axs.set_ylim(top=150000)
    plt.show()
    print(statistics.mean(data))


def all_six_numbers_on_die():
    view_numbers = []
    rolls = 0

    while len(view_numbers) < 6:
        num = random.randrange(1, 7)
        if num not in view_numbers:
            view_numbers.append(num)
        rolls += 1

    return rolls

def experiment():
    rounds = 100000
    num_rolls = []
    for i in range(rounds):
        num_rolls.append(all_six_numbers_on_die())

    return statistics.mean(num_rolls)


print(experiment())


