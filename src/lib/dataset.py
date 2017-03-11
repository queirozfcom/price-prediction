import pandas as pd
import numpy as np


# the last column of the dataframe becomes y,
# all other numeric columns become input features (X)
def make_Xy_simple(df):
    X = []
    y = []
    
    for nparr in df.values:
        y.append(nparr[-1])
        X.append(nparr[0:-1].tolist())
    
    return (np.array(X),np.array(y))
    
    