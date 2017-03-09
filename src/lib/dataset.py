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
    
    return np.array(X),np.array(y)


# takes a pandas dataframe and returns a X matrix (input) and a y vector (outputs)
# resulting from using N previous infos to predict the next point.

# the first column is expected to be the timestamp, the last column is expected to be the column that
# will be our output (y)

# this dataframe should NOT have any duplicate rows and rows must be sorted according to their timestamps,
# in increasing fashion. I could verify this in the function body but I've decided not to, to make the example clearer

def make_Xy_lagged_model(df, delta=None, n=None):
        
    timestamp_col = df.iloc[:,0]

    # http://docs.python-guide.org/en/latest/writing/gotchas/#mutable-default-arguments
    if delta is not None:
        delta = pd.tslib.Timedelta('1 days')
    if n is not None:
        n = 3   

    # these are the timestamps of the days we can use as targets
    available_targets = []

    # for every element, see whether it can be used as a target, i.e. it needs 
    # at least N previous values available
    for i in range(len(timestamp_col)-1,n-1,-1):
        print(i)

        can_be_target = True

        # we compare the elements in the window in a pair wise manner
        for k in range(n):
            if abs(timestamp_col[i-k] - timestamp_col[i-k-1]) != delta:
                can_be_target=False
                break

        if can_be_target:        
            available_targets.append(timestamp_col[i])        

    # need to sort them because they were filled in in reverse order, due to my algorithm        
    y = sorted(available_targets)

    for target_timestamp in y:
        # this means: get me the index of the row whose 1st column equals this values
        indices = df[df.iloc[:,0] == target_timestamp].index.tolist()
                     
        # we've asked the caller to make sure the dataframe had unique keys... but if it does we must throw an error:
        try:
            index = indices[0]
        except IndexError:
            print("The dataframe to be 'transformed' must have a single row per time stamp.")
            
        # so a single row in the new, transformed, dataset will be:    
                     
    
    