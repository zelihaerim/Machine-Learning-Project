import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
from colorama import Fore, Style
import time

class Timer:    
    def __enter__(self):
        self.tick = time.time()
        return self
    def __exit__(self, *args, **kwargs):
        self.tock = time.time()
        self.elapsed = self.tock - self.tick

# check nan values ratios
def check_nan_value_ratio(df):
    nan_ratios = df.isna().sum() / len(df)
    for i, ind in enumerate(nan_ratios):
        percentage = ind * 100 
        formatted_percentage = f"%{percentage:.5f}"
        print(f"{nan_ratios.index[i]} : {formatted_percentage}")

def find_continuous_columns(df)->[]:
    continuous_columns = [col for col in df.select_dtypes(include='number').columns if df[col].nunique() > 10]
    print("Continuous Features:", continuous_columns)
    return continuous_columns
    
def detect_outliers(df,features):
    outlier_indices = []
    for c in features:
        # 1st quartile
        Q1 = np.percentile(df[c],25)
        # 3rd quartile
        Q3 = np.percentile(df[c],75)
        # IQR
        IQR = Q3 - Q1
        # Outlier step
        outlier_step = IQR * 1.5
        # detect outlier and their indeces
        outlier_list_col = df[(df[c] < Q1 - outlier_step) | (df[c] > Q3 + outlier_step)].index
        # store indeces
        outlier_indices.extend(outlier_list_col)
    outlier_indices = Counter(outlier_indices)
    multiple_outliers = list(i for i, v in outlier_indices.items() if v > 2)
    return multiple_outliers

