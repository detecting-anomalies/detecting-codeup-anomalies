#Imports
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


#compute bollinger bands
def compute_bollinger(series, column, span, k):

    mean_df = series.ewm(span=span).mean()
    std_df = series.ewm(span=span).std()
    upper_band = mean_df + std_df * k
    lower_band = mean_df - std_df * k
    final_df = pd.concat([series, mean_df, upper_band, lower_band], axis= 1)
    final_df.columns = [column, 'midband', 'ub', 'lb']
    final_df['pct_b'] = (final_df[column] - final_df['lb']) / (final_df['ub'] - final_df['lb'])

    return final_df



#plot exponential moving average
def plot_ema(df, title):
    plt.figure(figsize=(13, 7))
    plt.plot(df, label='Original')
    plt.xlabel('Date')
    plt.ylabel('Number of hits')
    plt.title(f'{title}EMA of website hits over time')
    plt.legend()
    plt.show()


# 2 new dfs, Data Science and Web Dev
def seperate_programs(df):
    '''
    makes 2 new dfs from original df, 1 for data science 
    students and the other for web dev students
    '''
    #program_id 3 is Data Science, this pulls all rows with 3 for program_id
    datsci_df = df.loc[df['program_id'] == 3]
   
    webdev_df1 = df.loc[df['program_id'] == 1 ]
    webdev_df2 = df.loc[df['program_id'] == 2 ]
    webdev_df4 = df.loc[df['program_id'] == 4 ]

    webdev_df = pd.concat([webdev_df1, webdev_df2, webdev_df4])



    return datsci_df, webdev_df