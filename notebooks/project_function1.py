# Mel's functions

import pandas as pd
import numpy as np

# Method Chain 1: Clean Data

def load_and_process(file, keep, maxim, drop):
    '''
    A function to load the value and process it as needed.
    Reads the file,
    Drops unused columns,
    Drops rows above maximum keep value,
    Resets the index
    
    Arguments:
    file - A file to read (required)
    keep - A column that is being kept, but need to remove some rows (required)
    maxim - The maximum value in the kept row (required)
    drop - columns that need to be dropped (required)
    '''
    df = pd.read_csv(file, sep='\t')
    df2 = (df.drop(drop, axis=1)
           .copy()[(df[keep] <= maxim) & (df!=0).all(axis=1)]
           .copy().reset_index(drop=True))
    return df2


# Mel's functions

def negative(df, cols):
    '''
    A funtion to create a negative value for the items that are reverse scored.
    Takes the value and creates it as a negative in a new dataframe.
    Then attaches it to a dataframe with the remaining columns.
    
    Arguments:
    df - a dataframe (required)
    cols - the columns to be used (required)
    '''
    df2 = -df[cols]
    df3 = df.drop(df[cols], axis=1)
    newFrame = [df3, df2]
    df4 = pd.concat(newFrame, axis=1)
    return df4

def sumcol(df, col1, col2, col3, col4, col5, col6, col7, col8, col9, col10):
    '''
    A funtion to sum the value of the total score of a trait
    Takes all values and sums them
    
    Arguments:
    df - a dataframe (required)
    col1-col10 - The colums that need to be summed (required)
    '''
    return df[col1]+df[col2]+df[col3]+df[col4]+df[col5]+df[col6]+df[col7]+df[col8]+df[col9]+df[col10]

def agegroup(df, upper, lower):
    '''
    A function to group ages together from the dataframe.
    It takes all the values from the age groups wanted creates a new data frame with just those.
    
    Arguments:
    df - a dataframe (required)
    upper - The upper age limit of group (does not include this number) (required)
    lower - the lower age limit of this group (required)
    '''
    df2 = df[df.age < upper]
    df2 = df2[df2.age >= lower]
    return df2

