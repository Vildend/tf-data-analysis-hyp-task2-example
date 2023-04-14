import pandas as pd
import numpy as np

from scipy.stats import anderson_ksamp

chat_id = 897901830 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    stat, pval = anderson_ksamp([x, y])
    return pval < 0.06
