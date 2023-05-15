import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



def select_col():
    url = 'dataset/data.csv'
    data = pd.read_csv(url)

    # Creating Pipeline
    corrs = data.corrwith(data['Bankrupt?'], method='pearson')
    selected_col = corrs[(corrs>.2) | (corrs <-.2)].index.tolist()[1:]
    return selected_col