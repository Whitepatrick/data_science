import numpy as np
import pandas as pd
from scipy import stats

def t_mean(mean_1, mean_2, arr_len):
    count = 0
    for i in xrange(10000):
        array_1 = np.random.normal(mean_1, 1, arr_len)
        array_2 = np.random.normal(mean_2, 1, arr_len)

        return stats.ttest_ind(array_1, array_2)



print t_mean(1, 1, 100)
