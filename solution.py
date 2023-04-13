import pandas as pd
import numpy as np


chat_id = 897901830 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    pval = anderson_ksamp([x, y]).pvalue
    return pvalue < 0.06
