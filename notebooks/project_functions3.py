#Minju's .py file

import pandas as pd

def reverseScoring(df, high, cols):
    '''
    Reverse scores on given column(s).
    
    Arguments:
    df - the data frame
    high - (int) the highest score available
    cols - the column(s) to reverse
    '''
    df[cols] = high - df[cols]
    return df

def load_and_process(csv_file):
    '''
    Load, process, reverse score, and create factor total score columns.
    
    Arguments:
    csv_file - a path to a .csv file
    '''
    #Method Chain 1
    df_1 = (pd.read_csv("../data/raw/data.csv", sep='\t')
    .copy().drop(['age', 'engnat', 'gender', 'hand', 'source', 'country'], axis=1))
    
    #Reverse Scoring
    df_1 = reverseScoring(df_1, 6, cols=['E2','E4','E6','E8','E10','N1','N3','N5','N6','N7','N8','N9','N10','A1','A3','A5','A7','C2','C4','C6','C8','O2','O4','O6'])

    #Method Chain 2
    df_2 = (pd.DataFrame(df_1)
        .assign(E_Total=lambda x: df_1.loc[:, 'E1':'E10'].sum(axis=1))
        .assign(N_Total=lambda x: df_1.loc[:, 'N1':'N10'].sum(axis=1))
        .assign(A_Total=lambda x: df_1.loc[:, 'A1':'A10'].sum(axis=1))
        .assign(C_Total=lambda x: df_1.loc[:, 'C1':'C10'].sum(axis=1))
        .assign(O_Total=lambda x: df_1.loc[:, 'O1':'O10'].sum(axis=1)))
    return df_2