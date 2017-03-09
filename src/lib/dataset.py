import pandas as pd
import numpy as np

   
def make_Xy_simple(dataframe):
    
    X = []
    y = []

    for nparr in dataframe.values:
        X.append(nparr[:-1].tolist())
        y.append(nparr[-1])

    return np.array(X),np.array(y)    

