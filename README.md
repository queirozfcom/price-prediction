#teste-b2w

# project structure


# CAREFUL:

revenue = unit price * units sold

----------------

# todos


## presentation

- maybe two presentations, one for executives, one for technical audiences

- need to present **both** past behavious as well as current trends and predictions for the future.

#### exploratory data analysis

- what are the main dataset statistics? 

- earliest and most recent data 

- histogram per week/month/day

  - is the data balanced?

- histogram per pay type, per competitor

  - is the data balanced?

- histogram per revenue bucket (buckets of 10,100, 1000?)

  - is the data balanced?

 - outliers?

 - bad data?

## process

The first I felt I needed to do was to look at current frameworks and articles about time-series forecasting to avoid making silly mistakes.


#### first approach

The first approach was very naïve, it was just linear regression because sometimes really simple models give good results and are easy and cheap to build (also, you can give some kind of early information to decision-makers while you are still working on a more sophisticated model)

#### second approach

Take sequences of 5 samples (same competitor, same pay time) and try to predict the 5th point with the 4 previous points.

#### targets

- given a product and a price, how much will be sold
 
  - per unit time?

#### differentiating factors (show off?)

 - git (I'm using git)

 - sql

   - maybe load the data into a database and perform a couple of queries to extract aggregation information, etc?

 - clustering

   - products with similar price behaviour?


#### promising packages

- pyflux

- cesium

- rpy2

 - ....

#### overfitting

I shouldn't try too many algorithms

#### seasonality

Acknowledge and explain how it's affected my analysis, what I did to handle that

#### time series

Acknowledge it's a time series (double check)

- ARIMA?

- SARIMA

#### evaluation metrics

 - MAE (relative)

 - RMSE (relative)

- if data is skewed, probably better to use AUC?


#### things I would do if I had more time

- recurrent neural networks (RNNs), which are neural-networks that take sequence into account

  - e.g. LSTM?


------

### references

- [Time Series Analysis with Python Intermediate | SciPy 2016 Tutorial | Aileen Nielsen](https://www.youtube.com/watch?v=JNfxr4BQrLk)

### stuff to look at

- [https://research.fb.com/prophet-forecasting-at-scale/](https://research.fb.com/prophet-forecasting-at-scale/)

- [unplugg API for time series forecasting](http://unplu.gg/test_api.html)